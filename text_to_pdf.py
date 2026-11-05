#!/usr/bin/env python3
"""Convert a local UTF-8 text file into a paginated PDF."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a local UTF-8 .txt file into a paginated PDF."
    )
    parser.add_argument("input", type=Path, help="Input UTF-8 .txt file")
    parser.add_argument(
        "-s", "--save", type=Path,
        help="Destination folder (created if necessary). Defaults to the input folder.",
    )
    parser.add_argument(
        "-o", "--output", type=Path,
        help="PDF filename or path. Relative filenames are placed in the save folder.",
    )
    parser.add_argument(
        "--overwrite", action="store_true",
        help="Allow replacing an existing PDF.",
    )
    return parser


def resolve_output(input_path: Path, save_folder: Path | None, output: Path | None) -> Path:
    base_folder = save_folder if save_folder is not None else input_path.parent
    if output is None:
        return base_folder / f"{input_path.stem}.pdf"
    if output.is_absolute():
        return output
    return base_folder / output


def text_to_story(text: str):
    """Create flowables while preserving line breaks and leading spaces."""
    style = ParagraphStyle(
        "TextLine",
        fontName="Courier",
        fontSize=9,
        leading=12,
        spaceAfter=0,
        wordWrap="CJK",
        splitLongWords=True,
    )
    story = []
    for line in text.splitlines():
        if not line:
            story.append(Spacer(1, 5))
            continue
        line = line.expandtabs(4)
        escaped = escape(line).replace(" ", "&#160;")
        story.append(Paragraph(escaped, style))
    if not story:
        story.append(Paragraph("(empty file)", style))
    return story


def convert(input_path: Path, output_path: Path) -> None:
    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Input file is not valid UTF-8 text.") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=input_path.stem,
    )
    document.build(text_to_story(text))


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_path = args.input.expanduser()
    if not input_path.exists():
        parser.error(f"Input file does not exist: {input_path}")
    if not input_path.is_file():
        parser.error(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".txt":
        parser.error("Input file must have a .txt extension.")

    output_path = resolve_output(input_path, args.save, args.output).expanduser()
    if output_path.suffix.lower() != ".pdf":
        parser.error("Output filename must have a .pdf extension.")
    if output_path.exists() and not args.overwrite:
        parser.error(
            f"Output already exists: {output_path}. Use --overwrite to replace it."
        )

    try:
        convert(input_path, output_path)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(f"PDF created: {output_path.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
