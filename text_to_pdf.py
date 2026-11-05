#!/usr/bin/env python3
"""Convert local UTF-8 text files into paginated PDFs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from xml.sax.saxutils import escape

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert local UTF-8 .txt files into PDFs. Run without arguments for the interactive menu."
    )
    parser.add_argument("input", nargs="?", type=Path, help="Input UTF-8 .txt file")
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
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import Paragraph, Spacer
    style = ParagraphStyle(
        "TextLine", fontName="Courier", fontSize=9, leading=12,
        spaceAfter=0, wordWrap="CJK", splitLongWords=True,
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
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate
    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Input file is not valid UTF-8 text.") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output_path), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm, title=input_path.stem,
    )
    document.build(text_to_story(text))


def convert_checked(
    input_path: Path, save_folder: Path | None = None,
    output: Path | None = None, overwrite: bool = False,
) -> Path:
    input_path = input_path.expanduser()
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")
    if not input_path.is_file():
        raise ValueError(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".txt":
        raise ValueError("Input file must have a .txt extension.")

    output_path = resolve_output(input_path, save_folder, output).expanduser()
    if output_path.suffix.lower() != ".pdf":
        raise ValueError("Output filename must have a .pdf extension.")
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Output already exists: {output_path}. Use --overwrite to replace it."
        )
    convert(input_path, output_path)
    return output_path.resolve()


def choose_text_file() -> Path | None:
    """Open a local file picker when Tk is available; otherwise ask for a path."""
    try:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        root.update()
        selected = filedialog.askopenfilename(
            title="Choose a text file to convert",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        root.destroy()
        return Path(selected) if selected else None
    except (ImportError, RuntimeError, OSError):
        print("File picker is unavailable in this environment.")
        raw_path = input("Type the full path to your .txt file (or press Enter to cancel): ").strip()
        return Path(raw_path.strip('"')) if raw_path else None


def interactive_menu() -> int:
    # ANSI escape sequences color the banner in supported terminals.
    reset = "\\033[0m"
    green = "\\033[32m"
    bright_green = "\\033[1;92m"
    bold = "\\033[1m"
    print()
    print(bright_green + "████████╗███████╗██╗  ██╗████████╗" + reset)
    print(bright_green + "╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝" + reset)
    print(green + "   ██║   █████╗   ╚███╔╝    ██║   " + reset)
    print(green + "   ██║   ██╔══╝   ██╔██╗    ██║   " + reset)
    print(bright_green + "   ██║   ███████╗██╔╝ ██╗   ██║   " + reset)
    print(green + "   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   " + reset)
    print(bold + bright_green + "       T E X T  -  T O  -  P D F" + reset)
    print(green + "╔══════════════════════════════════════════════╗" + reset)
    print(green + "║" + reset + "       " + bold + bright_green + "YOUR TEXT. YOUR PDF. YOUR CONTROL." + reset + "       " + green + "║" + reset)
    print(green + "╚══════════════════════════════════════════════╝" + reset)
    print("Convert your plain-text files into clean PDFs.")
    print("Your files stay on this computer; nothing is uploaded.")
    while True:
        print("\n  [1] Choose a .txt file and convert it")
        print("  [2] Help — what does this tool do?")
        print("  [3] Commands and options")
        print("  [4] Troubleshooting guide")
        print("  [0] Exit")
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            chosen = choose_text_file()
            if chosen is None:
                print("Selection cancelled.")
                continue
            folder = input("Save folder (Enter = same folder as text file): ").strip()
            save_folder = Path(folder.strip('"')).expanduser() if folder else None
            overwrite = input("Replace an existing PDF if needed? [y/N]: ").strip().lower() == "y"
            try:
                result = convert_checked(chosen, save_folder, overwrite=overwrite)
                print(f"\n✓ PDF created: {result}")
            except (OSError, ValueError) as exc:
                print(f"\n✗ Could not convert: {exc}")
                print("Choose [4] Troubleshooting for help.")
        elif choice == "2":
            print("\nWHAT IT DOES")
            print("- Converts plain UTF-8 .txt files into paginated PDF documents.")
            print("- Keeps blank lines and indentation; wraps long lines.")
            print("- Creates output folders automatically.")
            print("- Protects existing PDFs unless you approve replacing them.")
            print("\nWHAT IT DOES NOT DO")
            print("- It does not directly convert .docx or .md files.")
            print("- It does not upload, scan, or transmit your files.")
            print("- You choose the file yourself using the file picker.")
        elif choice == "3":
            print("\nCOMMANDS")
            print("  python text_to_pdf.py                 Open this menu")
            print("  python text_to_pdf.py notes.txt       Convert beside the input")
            print("  python text_to_pdf.py notes.txt -s out")
            print("                                       Save into the ./out folder")
            print("  python text_to_pdf.py notes.txt -o Notes.pdf")
            print("  python text_to_pdf.py notes.txt --overwrite")
            print("\nOPTIONS: -s/--save FOLDER, -o/--output FILE.pdf, --overwrite, -h/--help")
        elif choice == "4":
            print("\nTROUBLESHOOTING")
            print("- No module named reportlab: install ReportLab for the Python you run.")
            print("- Ubuntu: sudo apt update && sudo apt install python3-reportlab")
            print("- Windows: python -m pip install reportlab (or py -m pip install reportlab)")
            print("- No module named pip: see troubleshooting/UBUNTU_PYTHON_PIP.md")
            print("- Python command not found: see troubleshooting/README.md")
            print("- File picker not opening: enter the full .txt path when prompted.")
            print("- Output already exists: choose another filename or approve overwrite.")
            print("- More detailed solutions: open the repository's troubleshooting folder.")
        elif choice == "0":
            print("See you next time!")
            return 0
        else:
            print("Please choose 0, 1, 2, 3, or 4.")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.input is None:
        return interactive_menu()

    try:
        output_path = convert_checked(args.input, args.save, args.output, args.overwrite)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(f"PDF created: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
