# Text-to-PDF

A small, cross-platform Python command-line tool that converts a local UTF-8 `.txt` file into a paginated PDF. **Your text stays on your computer**—the program does not upload or transmit files.

## Features

- Converts UTF-8 `.txt` files to PDF.
- Preserves line breaks, blank lines, indentation, and tabs (tabs expand to four spaces).
- Wraps long lines and supports multiple pages.
- Creates the destination folder when needed.
- Refuses to overwrite an existing PDF unless `--overwrite` is specified.
- Runs on Windows, macOS, and Linux.

## Requirements

- Python 3.10 or newer
- ReportLab

Install ReportLab:

```bash
python -m pip install -r requirements.txt
```

Or install the dependency directly:

```bash
python -m pip install reportlab
```

## Usage

```bash
python text_to_pdf.py docname.txt -s foldername
```

This creates `foldername/docname.pdf`. The folder is created automatically if it does not exist.

If `-s` is omitted, the PDF is saved beside the input file:

```bash
python text_to_pdf.py docname.txt
```

### Choose the PDF filename

```bash
python text_to_pdf.py docname.txt -s output -o notes.pdf
```

A relative output filename is placed in the selected save folder. An absolute output path is used as given.

### Replace an existing PDF

By default, existing files are protected:

```bash
python text_to_pdf.py docname.txt --overwrite
```

## Download and run

### macOS / Linux / Git Bash

```bash
wget https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py
python -m pip install reportlab
python text_to_pdf.py docname.txt -s foldername
```

### Windows PowerShell

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -OutFile "text_to_pdf.py"
py -m pip install reportlab
py text_to_pdf.py docname.txt -s foldername
```

If `py` is unavailable, use `python` instead.

## Options

| Option | Description |
|---|---|
| `-s`, `--save FOLDER` | Destination folder; created if needed. Defaults to the input file's folder. |
| `-o`, `--output FILE.pdf` | Choose the output PDF filename or path. |
| `--overwrite` | Explicitly allow replacing an existing PDF. |

## Run tests

```bash
python -m pip install -r requirements.txt
python -m unittest -v
```

## Privacy

The tool performs conversion locally using Python and ReportLab. It does not make network requests or upload your text.

## License

MIT. See [LICENSE](LICENSE).
