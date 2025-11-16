#!/usr/bin/env python3
"""
generate_prompts.py

Generate a full multi-chapter technical book from a YAML definition.

Features:
 - Supports seed files (existing chapter text)
 - Generates one output file per section
 - Maintains a rolling summary of all previous chapters
 - Injects future outline + previous summary + section/chapter intent
 - Produces MkDocs-aligned output folder structure
 - Uses OpenAI Responses API
 - Jinja2 templating for the main prompt
 - Token-safe summaries (model summarises text on every iteration)

Folder layout produced:

output/
    chapters/
        chapter_01/
            section_01_full_chapter.md
        chapter_02/
            section_01_modern_product_landscape.md
            section_02_introducing_cornerstone.md
            ...
    summary/
        summary_to_date.md

Dependencies:
    pip install pyyaml jinja2 openai

Environment:
    export OPENAI_API_KEY="xxx"
"""

import argparse
import logging
import os
import re
from typing import Dict, Any, List

import yaml
from jinja2 import Template
from openai import OpenAI

logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# Logging
# ------------------------------------------------------------
def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def kebab(s: str) -> str:
    """Convert a title into a safe kebab-style filename."""
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_template(template_str: str, context: Dict[str, Any]) -> str:
    template = Template(template_str)
    return template.render(**context)


# ------------------------------------------------------------
# OpenAI Calls
# ------------------------------------------------------------
def call_openai(prompt: str) -> str:
    """Return full text output."""
    client = OpenAI()
    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        max_output_tokens=8192,
    )
    return resp.output_text


def call_openai_summary(text: str) -> str:
    """Summarise text into a compact rolling summary."""
    client = OpenAI()
    prompt = (
        "Summarise the following book content in a compact, high-level form, "
        "maintaining terminology, key concepts, and tone. "
        "Do NOT add new content.\n\n"
        f"{text}"
    )
    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        max_output_tokens=2048,
    )
    return resp.output_text


# ------------------------------------------------------------
# Core Logic
# ------------------------------------------------------------
def process_book(yaml_data: Dict[str, Any], output_dir: str) -> None:
    template_str = yaml_data["template"]
    book_meta = yaml_data["book"]
    chapters = yaml_data["chapters"]

    # Ensure folder layout
    chapters_root = os.path.join(output_dir, "chapters")
    summary_root = os.path.join(output_dir, "summary")
    os.makedirs(chapters_root, exist_ok=True)
    os.makedirs(summary_root, exist_ok=True)

    summary_path = os.path.join(summary_root, "summary_to_date.md")
    rolling_summary = ""

    for chapter in chapters:
        chap_no = chapter["number"]
        chap_title = chapter["title"]
        chap_dir = os.path.join(chapters_root, f"chapter_{chap_no:02d}")
        os.makedirs(chap_dir, exist_ok=True)

        logger.info(f"Processing Chapter {chap_no}: {chap_title}")

        # Build future outline
        future_outline = [
            f"{c['number']}. {c['title']}"
            for c in chapters
            if c["number"] > chap_no
        ]
        future_outline_text = "\n".join(future_outline) or "(no further chapters)"

        # Handle seed chapter
        if "seed_file" in chapter:
            seed_path = chapter["seed_file"]
            logger.info(f"Chapter {chap_no}: using seed file {seed_path}")
            with open(seed_path, "r", encoding="utf-8") as f:
                seed_text = f.read()

            # Write seed as a single section
            out_file = os.path.join(chap_dir, "section_01_full_chapter.md")
            with open(out_file, "w", encoding="utf-8") as out:
                out.write(seed_text)

            # Add to rolling summary
            rolling_summary = call_openai_summary(rolling_summary + "\n" + seed_text)
            with open(summary_path, "w", encoding="utf-8") as s:
                s.write(rolling_summary)

            continue

        # Non-seed chapter → process each section
        for idx, section in enumerate(chapter["sections"], start=1):
            sec_title = section["title"]
            logger.info(f"Section {idx}: {sec_title}")

            # Prepare context
            context = {
                "book": book_meta,
                "chapter": chapter,
                "section": section,
                "previous_summary": rolling_summary or "(no previous content)",
                "future_outline": future_outline_text,
            }
            prompt = render_template(template_str, context)

            # Call OpenAI
            generated_text = call_openai(prompt)

            # Write section file
            safe_name = f"section_{idx:02d}_{kebab(sec_title)}.md"
            out_path = os.path.join(chap_dir, safe_name)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(generated_text)

            # Update rolling summary
            rolling_summary = call_openai_summary(rolling_summary + "\n" + generated_text)
            with open(summary_path, "w", encoding="utf-8") as s:
                s.write(rolling_summary)


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate a full book from book.yaml.")
    parser.add_argument("yaml_file", help="Input book YAML file")
    parser.add_argument("output_dir", help="Output directory (MkDocs structure)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logs")

    args = parser.parse_args()
    setup_logging(args.verbose)

    yaml_data = load_yaml(args.yaml_file)
    process_book(yaml_data, args.output_dir)


if __name__ == "__main__":
    main()
