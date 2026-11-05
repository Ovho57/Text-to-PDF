# Text-to-PDF (Linux / Ubuntu)

A beginner-friendly Python program that converts UTF-8 `.txt` files into paginated PDF documents. It is supported **on Linux/Ubuntu only**.

Your files stay on your computer. The converter does not upload or transmit them.

## Features

- Convert plain text files to PDF.
- Preserve line breaks, blank lines, and indentation.
- Wrap long lines and create multiple PDF pages.
- Choose files using a graphical picker (when available).
- **Browse folders and files from the terminal** when you want to navigate manually.
- Set a different PDF output folder.
- Avoid overwriting an existing PDF unless you approve it.

> Word (`.docx`) and Markdown (`.md`) files are not directly supported. Export or save them as `.txt` first.

## Quick start: Ubuntu

### 1. Install dependencies

Open Ubuntu Terminal and run:

```bash
sudo apt update
sudo apt install -y python3 python3-reportlab python3-tk git
```

### 2. Download the repository

```bash
git clone https://github.com/Ovho57/Text-to-PDF.git
cd Text-to-PDF
```

If you already downloaded it, update the existing folder instead:

```bash
cd ~/Text-to-PDF
git pull
```

### 3. Start the program

```bash
python3 text_to_pdf.py
```

### 4. Menu options

- **1 — Choose a .txt file and convert it:** opens a graphical file picker if available.
- **2 — Browse folders and files:** navigate folders in the terminal, list their contents, and select a text file.
- **3 — Help:** learn what the program does.
- **4 — Commands and options:** view command-line examples.
- **5 — Troubleshooting:** see common fixes.
- **0 — Exit.**

The PDF is saved beside the original text file by default. You can enter a different output folder when asked.

## Browse files from the terminal

Choose menu option **2**. When asked for a folder, type the directory you want to explore. For example:

```text
/mnt/c/Users/DELL/Desktop
```

The browser lists files and folders. Type a folder's number to enter it, `..` to go to the parent folder, or `q` to cancel. Select a `.txt` file by entering its number.

For other directories, enter their full Linux path. Paths with spaces should be wrapped in quotes when typed as a command.

## Ubuntu under Windows (WSL): access Windows files

If Ubuntu is installed through WSL (Windows Subsystem for Linux), Windows drives are normally mounted under `/mnt/`.

- Windows C: drive → `/mnt/c/`
- Windows Desktop → often `/mnt/c/Users/DELL/Desktop`
- Windows Downloads → often `/mnt/c/Users/DELL/Downloads`

Your Windows username may not be `DELL`. Find the correct folder:

```bash
ls /mnt/c/Users
```

Then list Desktop files (replace `YOUR_USERNAME`):

```bash
ls "/mnt/c/Users/YOUR_USERNAME/Desktop"
```

To change into the Windows Desktop directory:

```bash
cd "/mnt/c/Users/YOUR_USERNAME/Desktop"
```

To open Windows File Explorer at your current WSL folder:

```bash
explorer.exe .
```

### Example: converting a Windows Desktop text file

```bash
python3 ~/Text-to-PDF/text_to_pdf.py "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt"
```

The resulting PDF is normally created beside `notes.txt`, unless you specify another output location.

## Move or copy files between Ubuntu and Windows

### Copy a Windows file into Ubuntu

Example: copy a text file from Windows Desktop to your Ubuntu home folder:

```bash
cp "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt" ~/
```

### Move a Windows file into Ubuntu

```bash
mv "/mnt/c/Users/YOUR_USERNAME/Desktop/notes.txt" ~/
```

**Note:** `mv` removes it from the original Windows folder after moving. Use `cp` if you want to keep the original.

### Copy a PDF from Ubuntu to Windows Desktop

```bash
cp ~/Text-to-PDF/notes.pdf "/mnt/c/Users/YOUR_USERNAME/Desktop/"
```

Replace the example filenames and username with your actual ones.

## Command-line usage

Run commands from inside the repository:

```bash
cd ~/Text-to-PDF
```

Convert a text file (PDF beside source):

```bash
python3 text_to_pdf.py notes.txt
```

Save into a specific folder (it will be created if needed):

```bash
python3 text_to_pdf.py notes.txt --save output
```

Set the PDF filename:

```bash
python3 text_to_pdf.py notes.txt --output Notes.pdf
```

Allow replacing an existing PDF:

```bash
python3 text_to_pdf.py notes.txt --overwrite
```

Paths containing spaces need quotation marks:

```bash
python3 text_to_pdf.py "Biology ocho.txt"
```

## Troubleshooting

### `python3: command not found`

```bash
sudo apt update
sudo apt install -y python3
```

### `No module named reportlab`

```bash
sudo apt install -y python3-reportlab
```

### File picker does not open

Install Tkinter:

```bash
sudo apt install -y python3-tk
```

Or use menu option **2 — Browse folders and files**. You can also run the script with a file path directly.

### `can't open file ... text_to_pdf.py`

Check your current folder:

```bash
pwd
ls -la
```

Go to the project directory:

```bash
cd ~/Text-to-PDF
```

The script is named **`text_to_pdf.py`** (underscores, not hyphens).

### `Input file does not exist`

Check the exact location and filename:

```bash
ls "/path/to/the/folder"
```

If the filename has spaces, wrap the entire path in double quotes. In WSL, Windows files are usually under `/mnt/c/Users/`.

### PDF already exists

Choose a different filename or use `--overwrite` if you intend to replace the old PDF.

### Permission denied

Choose a folder you own, such as your Ubuntu home directory or Windows Desktop through WSL. Avoid running the converter with `sudo`.

## Verify ReportLab

```bash
python3 -c "import reportlab; print('ReportLab is installed')"
```

## Run tests

```bash
python3 -m unittest -v
```

## License

MIT. See [LICENSE](LICENSE).
