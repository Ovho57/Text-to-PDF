# Text-to-PDF

A Python text-to-PDF utility with a beginner-friendly interactive terminal menu and command-line mode. It converts local UTF-8 `.txt` files into paginated PDFs. **Your text stays on your computer**—the program does not upload or transmit files.

## What this tool does

- Converts plain-text `.txt` files to PDF.
- Keeps line breaks, blank lines, indentation, and tabs (tabs expand to four spaces).
- Wraps long lines and supports multiple PDF pages.
- Creates the destination folder automatically.
- Protects existing PDFs from accidental replacement.
- Runs on Windows, macOS, and Linux.\n- Opens an interactive menu when launched without arguments.\n- Lets you choose a local text file with a file picker (or type its path if the picker is unavailable).\n- Includes Help, Commands, and Troubleshooting menu sections.

> **Note:** This tool converts plain text. It does not convert Word files (`.docx`) or Markdown files (`.md`) directly. Copy/export those to plain text first.

---

## Quick start: interactive menu\n\nRun the script without a filename to open the menu:\n\nWindows:\n\n```cmd\npython text_to_pdf.py\n```\n\nUbuntu/Linux:\n\n```bash\npython3 text_to_pdf.py\n```\n\nChoose **1** to browse for a `.txt` file and convert it. The file picker only accesses the file you select; it does not upload anything. Choose **2** for Help, **3** for commands, or **4** for troubleshooting. Some Ubuntu/WSL environments do not have a desktop file picker; in that case, type the full path when prompted.\n\nFor detailed fixes, see the [Troubleshooting Center](troubleshooting/README.md).\n\n## 1. What you need

Before using the tool, make sure you have:

1. A computer (Windows, macOS, or Linux).
2. Python **3.10 or newer**.
3. An internet connection for the initial download and dependency installation.
4. A text file ending in `.txt`, such as `biology.txt`.
5. A terminal: Command Prompt, PowerShell, Windows Terminal, or macOS/Linux terminal.

### Install Python on Windows

1. Go to the official Python download page: https://www.python.org/downloads/
2. Download a current Python 3 version.
3. Run the installer.
4. If the installer offers **Add Python to PATH**, select it.
5. Finish installation.
6. Close and reopen your terminal.
7. Check that Python is installed:

Command Prompt or PowerShell:

```cmd
py --version
```

If that command does not work, try:

```cmd
python --version
```

You should see a Python version number. If neither command works, see [Python is not recognized](#python-is-not-recognized).

### macOS / Linux

Check Python:

```bash
python3 --version
```

Install Python 3.10+ using your operating system's official package or Python's official website if needed.

---

## 2. Download the script

You can download only the script—Git is not required.

### Windows Command Prompt (CMD)

Open CMD in the folder where you want the tool and run:

```cmd
curl -L "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -o text_to_pdf.py
```

### Windows PowerShell

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -OutFile "text_to_pdf.py"
```

### macOS / Linux / Git Bash

```bash
curl -L "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -o text_to_pdf.py
```

The downloaded file should be named `text_to_pdf.py`.

**CMD vs PowerShell:** `Invoke-WebRequest` is a PowerShell command. If CMD says it is not recognized, use the `curl` command above instead.

---

## 3. Install the required library

This project uses ReportLab to create PDFs.

### Windows

```cmd
py -m pip install reportlab
```

If `py` is unavailable but `python` works:

```cmd
python -m pip install reportlab
```

### macOS / Linux

```bash
python3 -m pip install reportlab
```

### If you downloaded the entire repository

From inside the repository folder, install its requirements:

```bash
python -m pip install -r requirements.txt
```

---

## 4. Prepare your text file

Create a plain-text file in Notepad, VS Code, or another text editor.

Example filename:

```text
biology.txt
```

Save it as **Plain Text** with the `.txt` extension and UTF-8 encoding if your editor offers an encoding option.

For the easiest first try, put these two files in the same folder:

- `text_to_pdf.py`
- `biology.txt`

### Check the file extension

Windows may hide extensions. Make sure the file is really `biology.txt`, not `biology.txt.txt` or `biology.docx`.

In File Explorer, you can enable **View → Show → File name extensions**.

---

## 5. Open a terminal in the correct folder

The terminal needs to be in the folder containing `text_to_pdf.py` and your text file (unless you use full paths).

### Easy method in Windows

1. Open the folder in File Explorer.
2. Click the address bar.
3. Type `cmd` and press Enter. (For PowerShell, type `powershell`.)
4. The terminal opens in that folder.
5. Run:

```cmd
dir
```

You should see `text_to_pdf.py` and your text file listed.

---

## 6. Convert your first file

### Basic command

Windows:

```cmd
py text_to_pdf.py biology.txt
```

macOS / Linux:

```bash
python3 text_to_pdf.py biology.txt
```

If you omit the save-folder option, the PDF is saved beside the input text file.

### Save the PDF to a folder

```cmd
py text_to_pdf.py biology.txt -s output
```

This creates the `output` folder if needed and saves:

```text
output/biology.pdf
```

### Save directly to your Windows Desktop

```cmd
py text_to_pdf.py biology.txt -s "%USERPROFILE%\Desktop"
```

PowerShell:

```powershell
py text_to_pdf.py biology.txt -s "$HOME\Desktop"
```

### Choose a custom PDF name

```cmd
py text_to_pdf.py biology.txt -s output -o Biology-Notes.pdf
```

### Use paths that contain spaces

Put paths in quotation marks:

```cmd
py text_to_pdf.py "My Biology Notes.txt" -s "My PDFs"
```

### Use full paths if your files are in different folders

```cmd
py "C:\Users\YourName\Downloads\text_to_pdf.py" "C:\Users\YourName\Documents\biology.txt" -s "C:\Users\YourName\Desktop"
```

Replace `YourName` with your Windows account folder name.

---

## 7. Command options

| Option | Meaning |
|---|---|
| `-s FOLDER` or `--save FOLDER` | Folder where the PDF should be saved. It is created automatically. |
| `-o FILE.pdf` or `--output FILE.pdf` | Set the output PDF filename/path. |
| `--overwrite` | Allow replacing an existing PDF. |

### Important: existing files are protected

If a PDF with the same name already exists, the program stops rather than deleting it.

To replace it intentionally:

```cmd
py text_to_pdf.py biology.txt -s output --overwrite
```

Use `--overwrite` only when you really want to replace the old PDF.

---

## 8. Common errors and solutions

### Error: `'Invoke-WebRequest' is not recognized...`

**Cause:** You typed a PowerShell command in Command Prompt (CMD).

**Fix:** In CMD, download with:

```cmd
curl -L "https://raw.githubusercontent.com/Ovho57/Text-to-PDF/main/text_to_pdf.py" -o text_to_pdf.py
```

Or open PowerShell and use `Invoke-WebRequest`.

### Error: `'py' is not recognized` or `'python' is not recognized`

**Cause:** Python may not be installed, or Windows cannot find it.

**Fix:**
1. Install Python from https://www.python.org/downloads/
2. Select **Add Python to PATH** if shown.
3. Close and reopen your terminal.
4. Try `py --version`, then `python --version`.

### Error: `No module named pip`

**Fix (Windows):**

```cmd
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip install reportlab
```

If using `python` instead of `py`, replace the command prefix accordingly.

### Error: `No module named reportlab`

**Cause:** ReportLab is not installed for the Python interpreter you're using.

**Fix:**

```cmd
py -m pip install reportlab
```

Then run the converter with the same Python command (`py`). If you run it with `python`, install using `python -m pip install reportlab`.

### Error: `can't open file 'text_to_pdf.py'`

**Cause:** The terminal is in the wrong folder, or the script has a different name.

**Fix:**
1. Run `dir` in CMD or `ls` in PowerShell/macOS/Linux.
2. Check that `text_to_pdf.py` appears.
3. Navigate to the folder using `cd "full path to folder"`, or run the script using its full path.

### Error: input file not found

**Cause:** The text filename/path is incorrect or the terminal is in the wrong folder.

**Fix:** Check the filename with `dir`. Include the full path and quotation marks if it contains spaces.

### Error: input must be a .txt file

**Cause:** The file is not a plain-text `.txt` file.

**Fix:** Save/export it as plain text. A Word file such as `.docx` is not a text file; renaming it does not convert it.

### Error: output PDF already exists

**Cause:** The tool avoids overwriting files by default.

**Fix:** Choose a different output name, delete the old PDF yourself if you no longer need it, or use `--overwrite` intentionally.

### Error: permission denied / access denied

**Cause:** You may be trying to save to a protected folder, or the PDF may be open in a program that locks it.

**Fix:**
1. Save to a folder you own, such as Documents or Desktop.
2. Close the existing PDF in your PDF viewer before replacing it.
3. Try a different output filename.

### Error: pip cannot download / connection timed out

**Cause:** Internet connection, proxy, firewall, or package index issue.

**Fix:**
1. Check your internet connection.
2. Try again later.
3. Update pip:

```cmd
py -m pip install --upgrade pip
```

4. Retry:

```cmd
py -m pip install reportlab
```

### PDF displays some unusual characters incorrectly

**Cause:** The current PDF font may not include every Unicode character.

**Fix:** Try replacing unusual symbols with ordinary characters. Some emojis and rare scripts may not display correctly in the current version.

### PDF is blank or has unexpected text

**Fix:**
1. Open the original `.txt` file and confirm it contains text.
2. Confirm you passed the correct filename.
3. Try a short test file containing a few simple lines.

---

## 9. Verify installation

Windows:

```cmd
py -c "import reportlab; print('ReportLab installed successfully')"
```

macOS / Linux:

```bash
python3 -c "import reportlab; print('ReportLab installed successfully')"
```

If it prints the success message, ReportLab is available for that Python interpreter.

---

## 10. Run the project tests (contributors)

If you cloned or downloaded the repository source:

```bash
python -m pip install -r requirements.txt
python -m unittest -v
```

On Windows, you can use `py` instead of `python`.

---

## Privacy

Conversion happens locally on your computer. The script does not upload or transmit your text.

## License

MIT. See [LICENSE](LICENSE).
