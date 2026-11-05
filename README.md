# Text-to-PDF (Linux / Ubuntu)

A beginner-friendly Python tool for converting local UTF-8 `.txt` files into paginated PDFs. This project is supported **only on Linux, including Ubuntu**.

Your files stay on your computer. The program does not upload or transmit them.

## Features

- Converts plain-text `.txt` files to PDF.
- Preserves line breaks, blank lines, indentation, and tabs.
- Wraps long lines and supports multi-page PDFs.
- Interactive terminal menu with Help, Commands, and Troubleshooting.
- GUI file picker when a desktop environment and Tkinter are available.
- Terminal path entry when the file picker is unavailable.
- Prevents accidental replacement of existing PDFs.

> It does not directly convert Word (`.docx`) or Markdown (`.md`) files. Save or export those as plain text first.

## Requirements

- Linux (Ubuntu recommended)
- Python 3.10+
- ReportLab
- Tkinter (optional; required only for the graphical file picker)

## Install on Ubuntu

Open Terminal and run:

```bash
sudo apt update
sudo apt install -y python3 python3-reportlab python3-tk git
```

Check Python:

```bash
python3 --version
```

## Download the project

Clone the repository:

```bash
git clone https://github.com/Ovho57/Text-to-PDF.git
cd Text-to-PDF
```

Or download just the script:

```bash
mkdir -p ~/Text-to-PDF
cd ~/Text-to-PDF
curl -L "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -o text_to_pdf.py
```

## Run the interactive menu

From the project directory:

```bash
python3 text_to_pdf.py
```

Choose **1** to select a `.txt` file and convert it. Choose **2** for Help, **3** for commands, **4** for troubleshooting, or **0** to exit.

If the graphical picker cannot open (for example, on Ubuntu Server or a headless terminal), the program asks you to enter the full path to the text file.

## Convert using terminal commands

Convert a file beside the source:

```bash
python3 text_to_pdf.py notes.txt
```

Save into a folder (created automatically):

```bash
python3 text_to_pdf.py notes.txt --save output
```

Choose a PDF filename:

```bash
python3 text_to_pdf.py notes.txt --output Notes.pdf
```

Replace an existing PDF only when you explicitly allow it:

```bash
python3 text_to_pdf.py notes.txt --overwrite
```

Use quotation marks for filenames or paths containing spaces:

```bash
python3 text_to_pdf.py "My Notes.txt" --save "My PDFs"
```

## Troubleshooting

### `python3: command not found`

Install Python:

```bash
sudo apt update
sudo apt install -y python3
```

### `No module named reportlab`

Install ReportLab from Ubuntu packages:

```bash
sudo apt install -y python3-reportlab
```

### File picker does not open

Install Tkinter:

```bash
sudo apt install -y python3-tk
```

If you are on a server or do not have a desktop environment, type the full path to your `.txt` file when prompted.

### `can't open file 'text_to_pdf.py'`

Check your current directory and files:

```bash
pwd
ls -la
```

Change to the project directory:

```bash
cd ~/Text-to-PDF
```

Confirm the filename is exactly `text_to_pdf.py` (underscores, not hyphens).

### Input file not found

Check the file path with `ls`. You can pass an absolute path:

```bash
python3 text_to_pdf.py "/home/your-user/Documents/notes.txt"
```

### PDF already exists

Choose another output filename or intentionally permit replacement using `--overwrite`.

### Permission denied

Save to a directory owned by your user, such as `~/Documents` or your project folder. Avoid using `sudo` to run the converter.

## Verify ReportLab

```bash
python3 -c "import reportlab; print('ReportLab is installed')"
```

## Run tests

From the repository folder:

```bash
python3 -m unittest -v
```

## License

MIT. See [LICENSE](LICENSE).
