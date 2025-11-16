#!/usr/bin/env python3
"""
generate_handbook.py

Generate a multi-section developer handbook from a structured YAML file.

Features:
 - Mirrors hierarchical folder structure defined in YAML
 - Creates one Markdown file per handbook page
 - Uses Jinja2 templates for prompt generation
 - Uses OpenAI Responses API for text generation
 - Designed for wiki / MkDocs-style documentation

Dependencies:
    pip install pyyaml jinja2 openai

Environment:
    export OPENAI_API_KEY="xxx"
"""

import argparse
import logging
import os
from typing import Dict, Any

import yaml
from jinja2 import Template
from openai import OpenAI


# ------------------------------------------------------------
# Logging
# ------------------------------------------------------------
def setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_template(template_str: str, context: Dict[str, Any]) -> str:
    return Template(template_str).render(**context)


def call_openai(prompt: str) -> str:
    """Return generated text using OpenAI Responses API."""
    client = OpenAI()
    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        max_output_tokens=8192,
    )
    return resp.output_text


# ------------------------------------------------------------
# Core Logic
# ------------------------------------------------------------
def process_handbook(yaml_data: Dict[str, Any], output_dir: str) -> None:
    """
    Expected YAML structure:

    handbook:
      title: "Developer Handbook"
      root: "developer_handbook"
      audience: ...
      description: ...

    template: |
       ... jinja2 template ...

    sections:
      - id: "01_intro"
        title: "Introduction"
        pages:
          - file: "overview.md"
            title: "Overview"
            intent: "Purpose..."
    """

    handbook_meta = yaml_data["handbook"]
    template_str = yaml_data["template"]
    sections = yaml_data["sections"]

    root_dir = os.path.join(output_dir, handbook_meta["root"])
    os.makedirs(root_dir, exist_ok=True)

    logging.info(f"Generating handbook into: {root_dir}")

    for section in sections:
        sec_id = section["id"]
        sec_title = section["title"]

        sec_dir = os.path.join(root_dir, sec_id)
        os.makedirs(sec_dir, exist_ok=True)

        logging.info(f"Section {sec_id}: {sec_title}")

        for page in section["pages"]:
            filename = page["file"]
            page_title = page["title"]

            logging.info(f"  -> Generating page {filename} ({page_title})")

            context = {
                "handbook": handbook_meta,
                "section": section,
                "page": page,
            }

            prompt = render_template(template_str, context)
            output_text = call_openai(prompt)

            out_path = os.path.join(sec_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(output_text)

    logging.info("Handbook generation complete.")


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate a developer handbook from YAML.")
    parser.add_argument("yaml_file", help="Handbook YAML definition")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()
    setup_logging(args.verbose)

    yaml_data = load_yaml(args.yaml_file)
    process_handbook(yaml_data, args.output_dir)


if __name__ == "__main__":
    main()
