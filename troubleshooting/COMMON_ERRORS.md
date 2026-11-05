# Common Text-to-PDF Errors

## `No module named reportlab`

Install ReportLab for the same Python you use to run the converter.

Ubuntu:

```bash
sudo apt update
sudo apt install python3-reportlab
```

Windows:

```cmd
python -m pip install reportlab
```

## `No module named pip`

Ubuntu: see [Ubuntu pip guide](UBUNTU_PYTHON_PIP.md); `apt install python3-reportlab` is often easiest.
Windows: after verifying Python is installed, try `python -m ensurepip --upgrade`.

## Python command not found

The interpreter may not be installed or on PATH. See [Windows Python guide](WINDOWS_PYTHON.md), or install Python through your Linux distribution.

## `Invoke-WebRequest` not recognized

That command is for PowerShell. CMD and Ubuntu use different commands; `curl` is commonly available in CMD/Linux.

## `can't open file text_to_pdf.py`

The terminal is likely in the wrong directory. Use `dir` on Windows or `ls` on Ubuntu, then `cd` into the project folder.

## Input file does not exist / must be `.txt`

Check the path, spelling, extension, and file format. Renaming a Word document to `.txt` does not convert it.

## PDF already exists

Choose another output filename or use `--overwrite` only when you intend to replace the existing PDF.

## File picker unavailable

Some Ubuntu/WSL or headless environments do not have a desktop picker. Enter the full file path when prompted.

## Permission denied

Save in a folder you own (for example, Documents) and close the PDF if your viewer has locked it.

## Still stuck?

Send the exact command, complete error text, operating system, and `python --version` or `python3 --version` output.