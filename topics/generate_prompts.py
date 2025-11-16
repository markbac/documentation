#!/usr/bin/env python3
"""
Generate model outputs from a template and a list of topic dictionaries.

This script:
  - Loads a YAML with:
        template: "<prompt...>"
        topics:
            - topic: "..."
              depth: "..."
              category: "..."
              sub_category: "..."   # optional
              output: "filename.ext"
  - Renders the template using Jinja2
  - Sends each prompt to the OpenAI Responses API
  - Saves each output under:
        <output_dir>/<category>/<sub_category?>/<output>

Notes:
  - If "output" already contains a path separator ("/" or os.sep), that path
    is used relative to output_dir and category/sub_category are ignored for
    compatibility.
  - If "category" is missing, files are written directly under output_dir.

API key MUST be provided via:
    export OPENAI_API_KEY="your_key_here"

Dependencies:
    pip install openai pyyaml jinja2
"""

import argparse
import logging
import os
import sys
from typing import Dict, Any, List

import yaml
from jinja2 import Template
from openai import OpenAI

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def require_api_key() -> None:
    """
    Ensure OPENAI_API_KEY exists; if missing, exit with instructions.
    """
    if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"].strip():
        print(
            "\nERROR: OPENAI_API_KEY is not set.\n\n"
            "Set it like this on Linux/macOS:\n"
            '    export OPENAI_API_KEY="your_key_here"\n\n'
            "Or on Windows PowerShell:\n"
            '    setx OPENAI_API_KEY "your_key_here"\n'
        )
        sys.exit(1)


def load_yaml(path: str) -> Dict[str, Any]:
    """Load YAML from file."""
    logger.debug(f"Loading YAML file: {path}")
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def render_template(template_str: str, context: Dict[str, Any]) -> str:
    """Render Jinja-style template with arbitrary fields."""
    logger.debug(f"Rendering template with context: {context}")
    template = Template(template_str)
    return template.render(**context)


def call_openai_api(prompt: str) -> str:
    """
    Send a prompt to the OpenAI Responses API.

    :param prompt: Fully rendered prompt.
    :return: Model output text.
    """
    logger.debug("Sending prompt to OpenAI API")
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt,
    )

    logger.debug("Received response from OpenAI API")

    # Use the convenience helper to extract text
    return response.output_text


def write_output(path: str, content: str) -> None:
    """Write output text to disk."""
    logger.debug(f"Writing output file: {path}")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def build_output_path(topic: Dict[str, Any], output_dir: str) -> str:
    """
    Build the output path using:
        <output_dir>/<category>/<sub_category?>/<output>

    Rules:
      - If topic["output"] already contains a path separator, treat it as a
        relative path under output_dir and ignore category/sub_category.
      - Otherwise, if category is present, use it as first directory.
      - If sub_category is present and non-empty, add it as a nested directory.
      - Finally append the output filename.
    """
    if "output" not in topic:
        raise KeyError("Topic is missing required field 'output'")

    raw_output = str(topic["output"])

    # If the user already supplied a path (e.g. "security/pki_overview.md"),
    # respect it and just make it relative to output_dir.
    if "/" in raw_output or os.sep in raw_output:
        out_path = os.path.join(output_dir, raw_output)
        logger.debug(
            "Topic has explicit path in 'output'; using: %s", out_path
        )
        return out_path

    category = topic.get("category")
    sub_category = topic.get("sub_category")

    parts: List[str] = [output_dir]

    if category:
        parts.append(str(category))

    if sub_category:
        parts.append(str(sub_category))

    parts.append(raw_output)

    out_path = os.path.join(*parts)
    logger.debug(
        "Auto-generated output path from category/sub_category: %s", out_path
    )
    return out_path


def process_topics(template_str: str, topics: List[Dict[str, Any]], output_dir: str) -> None:
    """Process each topic entry."""
    logger.info(f"Ensuring base output directory exists: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)

    for idx, topic in enumerate(topics):
        logger.info(f"Processing topic #{idx}: {topic.get('topic', '<no topic name>')}")

        try:
            out_path = build_output_path(topic, output_dir)
        except KeyError as exc:
            logger.error(f"Topic #{idx} error: {exc}")
            sys.exit(1)

        rendered_prompt = render_template(template_str, topic)
        logger.debug("Rendered prompt for topic #%d:\n%s", idx, rendered_prompt)

        result = call_openai_api(rendered_prompt)
        write_output(out_path, result)

        logger.info(f"Saved: {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate outputs from template + topic YAML."
    )
    parser.add_argument("yaml_file", help="Input YAML containing template + topics.")
    parser.add_argument(
        "output_dir",
        help="Base directory for output files (category/sub_category will be nested under this).",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logging."
    )

    args = parser.parse_args()

    setup_logging(args.verbose)
    require_api_key()

    data = load_yaml(args.yaml_file)

    template_str = data.get("template")
    topics = data.get("topics", [])

    if template_str is None:
        logger.error("YAML is missing required 'template' field.")
        sys.exit(1)

    if not isinstance(topics, list):
        logger.error("'topics' must be a list.")
        sys.exit(1)

    process_topics(template_str, topics, args.output_dir)


if __name__ == "__main__":
    main()
