![Text-to-PDF banner](assets/text-to-pdf-banner.svg)

<div align="center">

# Text-to-PDF

### Turn plain-text files into PDFs — right from your Linux terminal.

A lightweight, beginner-friendly Python utility for converting UTF-8 `.txt` files into clean, paginated PDF documents.

[**Get started**](#-quick-start) · [**Features**](#-features) · [**Usage**](#-usage) · [**Troubleshooting**](#-troubleshooting)

![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Ubuntu-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-open%20source-brightgreen)

</div>

---

## Why Text-to-PDF?

Need to turn text notes, documentation, or plain-text files into a PDF without a complicated workflow? **Text-to-PDF keeps it simple.**

- Your files stay on your computer — nothing is uploaded.
- Use the interactive terminal menu or run a command directly.
- Browse folders and files from the terminal with color-coded entries.
- Keep line breaks, blank lines, and indentation while handling long lines and multiple pages.

> **Platform:** Linux / Ubuntu only. Requires Python 3.10 or newer.  
> **File support:** UTF-8 `.txt` files. Word (`.docx`) and Markdown (`.md`) files are not directly supported; save or export them as plain text first.

## ✨ Features

| Feature | What it does |
| --- | --- |
| TXT → PDF | Convert UTF-8 text files into PDF documents |
| Smart text layout | Preserve line breaks, blank lines, indentation, and wrap long lines |
| Multi-page output | Create additional pages when needed |
| Interactive menu | Use a simple terminal menu to access tools |
| File picker | Choose a file graphically when available |
| Terminal file browser | Navigate folders and select files without a GUI |
| Color-coded browsing | Distinguish folders, TXT files, and other files |
| Flexible output | Save PDFs beside the source or in another folder |
| Overwrite protection | Avoid replacing an existing PDF without approval |

## 🐧 Quick start

### 1. Install dependencies

Open your Ubuntu terminal:

```bash
sudo apt update
sudo apt install -y python3 python3-reportlab python3-tk git
```

### 2. Clone the project

```bash
git clone https://github.com/Ovho57/Text-to-PDF.git
cd Text-to-PDF
```

Already cloned it? Update your local copy:

```bash
cd ~/Text-to-PDF
git pull
```

### 3. Run it

```bash
python3 text_to_pdf.py
```

That’s it — follow the terminal menu.

## 🧭 Menu overview

| Option | Action |
| --- | --- |
| `1` | Choose a `.txt` file and convert it (opens a graphical picker if available) |
| `2` | Browse folders and files in the terminal |
| `3` | Help |
| `4` | Commands and options |
| `5` | Troubleshooting |
| `0` | Exit |

### Color-coded file browser

When using menu option **2**, entries are color-coded to help you navigate:

- **Blue** — folders
- **Green** — `.txt` files
- **Yellow** — other files

Enter a folder’s number to open it, `..` to move to its parent folder, or `q` to cancel. Select a `.txt` file by entering its number.

## 📄 Usage

### Convert a file directly

Run from the project directory:

```bash
python3 text_to_pdf.py notes.txt
```

By default, the PDF is saved beside the original text file.

### Save the PDF in a specific folder

```bash
python3 text_to_pdf.py notes.txt --save output
```

The output folder will be created if needed.

### Choose the output filename

```bash
python3 text_to_pdf.py notes.txt --output Notes.pdf
```

### Replace an existing PDF

```bash
python3 text_to_pdf.py notes.txt --overwrite
```

### Paths with spaces

Wrap the path in quotation marks:

```bash
python3 text_to_pdf.py "Biology notes.txt"
```

## 🪟 Ubuntu on Windows (WSL)

If you use Ubuntu through Windows Subsystem for Linux, Windows drives are usually mounted under `/mnt/`.

| Windows location | Typical WSL path |
| --- | --- |
| C: drive | `/mnt/c/` |
| Desktop | `/mnt/c/Users/YOUR_USERNAME/Desktop` |
| Downloads | `/mnt/c/Users/YOUR_USERNAME/Downloads` |

Find your Windows username:

```bash
ls /mnt/c/Users
```

List Desktop files (replace `YOUR_USERNAME`):

```bash
ls "/mnt/c/Users/YOUR_USERNAME/Desktop"
```

Change to that directory:

```bash
cd "/mnt/c/Users/YOUR_USERNAME/Desktop"
```

Open Windows File Explorer at the current WSL directory:

```bash
explorer.exe .
```

### Convert a Windows Desktop file

```bash
python3 ~/Text-to-PDF/text_to_pdf.py "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt"
```

The PDF is usually created beside the text file unless you specify another output location.

### Move or copy files between Windows and Ubuntu

Copy a Windows file into Ubuntu:

```bash
cp "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt" ~/
```

Move it instead (this removes the original from its Windows folder):

```bash
mv "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt" ~/
```

Copy a PDF from Ubuntu to the Windows Desktop:

```bash
cp ~/Text-to-PDF/notes.pdf "/mnt/c/Users/YOUR_USERNAME/Desktop/"
```

Replace example filenames and usernames with your own.

## 🛠️ Troubleshooting

### `python3: command not found`

```bash
sudo apt update
sudo apt install -y python3
```

### `No module named reportlab`

```bash
sudo apt install -y python3-reportlab
```

### The file picker does not open

Install Tkinter:

```bash
sudo apt install -y python3-tk
```

Or use menu option **2 — Browse folders and files**, or run the program with a file path.

### `can't open file ... text_to_pdf.py`

Check your current directory:

```bash
pwd
ls -la
```

Then enter the project folder:

```bash
cd ~/Text-to-PDF
```

The script name is `text_to_pdf.py` (underscores, not hyphens).

### `Input file does not exist`

Check the exact path:

```bash
ls "/path/to/the/folder"
```

Use quotes around paths with spaces. In WSL, Windows files are usually under `/mnt/c/Users/`.

### PDF already exists

Choose another output filename or use `--overwrite` if you want to replace the existing PDF.

### Permission denied

Use a directory you own, such as your Ubuntu home folder or Windows Desktop through WSL. Avoid running the converter with `sudo`.

## 🧪 Verify ReportLab

```bash
python3 -c "import reportlab; print('ReportLab is installed')"
```

## 🧑‍💻 Run tests

```bash
python3 -m unittest -v
```

## 🤝 Contributions and feedback

Found a bug, have an idea, or want to improve the project? Feel free to open an issue or submit a pull request. Feedback and contributions are welcome.

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE).

---

<div align="center">

**Small tools. Useful solutions. Keep building.**

Made with Python for Linux / Ubuntu.

</div>
