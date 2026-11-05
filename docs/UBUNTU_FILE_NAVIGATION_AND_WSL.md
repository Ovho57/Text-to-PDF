# Ubuntu File Navigation and Windows/WSL Guide

This guide explains how to move around folders, locate files, and use the Text-to-PDF converter with files stored on Windows.

## 1. Basic Ubuntu commands

| Command | What it does |
| --- | --- |
| `pwd` | Prints the current directory |
| `ls` | Lists files and folders |
| `ls -la` | Lists everything, including hidden files |
| `cd foldername` | Enters a folder |
| `cd ..` | Goes up one folder |
| `cd ~` | Returns to your Ubuntu home directory |
| `mkdir foldername` | Creates a folder |
| `cp source destination` | Copies a file |
| `mv source destination` | Moves or renames a file |

Example:

```bash
cd ~/Text-to-PDF
pwd
ls -la
```

## 2. Windows files in Ubuntu WSL

If you're running Ubuntu inside Windows using WSL, Windows drives are available under `/mnt`.

Examples:

- C drive: `/mnt/c/`
- Windows user directories: `/mnt/c/Users/`
- Desktop: `/mnt/c/Users/USERNAME/Desktop`
- Downloads: `/mnt/c/Users/USERNAME/Downloads`

Find your actual Windows account folder:

```bash
ls /mnt/c/Users
```

Use the correct folder name in place of `USERNAME`.

To list files on Desktop:

```bash
ls "/mnt/c/Users/USERNAME/Desktop"
```

To enter Desktop:

```bash
cd "/mnt/c/Users/USERNAME/Desktop"
```

The quotation marks are important when a path contains spaces.

## 3. Open Windows Explorer from Ubuntu

To open File Explorer at the current directory:

```bash
explorer.exe .
```

To open a particular folder:

```bash
explorer.exe "/mnt/c/Users/USERNAME/Desktop"
```

## 4. Copy or move files

Copy a Windows text file to Ubuntu home:

```bash
cp "/mnt/c/Users/USERNAME/Desktop/notes.txt" ~/
```

Move it instead (this removes it from the original location):

```bash
mv "/mnt/c/Users/USERNAME/Desktop/notes.txt" ~/
```

Copy a PDF from Ubuntu to Windows Desktop:

```bash
cp ~/Text-to-PDF/notes.pdf "/mnt/c/Users/USERNAME/Desktop/"
```

**Tip:** Use `cp` when you want to keep the original. Use `mv` only when you want to move it.

## 5. Use the Text-to-PDF terminal browser

1. Open Ubuntu.
2. Run:

   ```bash
   cd ~/Text-to-PDF
   python3 text_to_pdf.py
   ```

3. Select menu option **2 — Browse folders and files**.
4. Enter a starting directory, such as:

   ```text
   /mnt/c/Users/USERNAME/Desktop
   ```

5. The program lists entries. Type the number beside a folder to enter it.
6. Type `..` to return to its parent folder.
7. Select a `.txt` file by its number.
8. Choose a save folder, or press Enter to save the PDF next to the original text file.
9. Confirm overwrite if a PDF with the same name already exists.

## 6. Convert directly from a Windows path

You can skip the menu and provide the file path:

```bash
python3 ~/Text-to-PDF/text_to_pdf.py "/mnt/c/Users/USERNAME/Desktop/notes.txt"
```

The PDF is created next to the text file by default.

## 7. Common mistakes

- **Typing a folder path by itself:** use `cd /mnt/c` to enter it. A folder path is not an executable command.
- **Wrong script spelling:** the file is `text_to_pdf.py`, with underscores.
- **Spaces in filenames:** use double quotes around the full path, e.g. `"Biology ocho.txt"`.
- **Wrong Windows username:** inspect `/mnt/c/Users` and use the actual directory name.
- **File not found:** use `ls` to inspect the folder and check spelling carefully.
- **PDF not in the folder you expected:** the converter normally saves beside the source file, unless you choose a different save directory.

## 8. Update the program from GitHub

```bash
cd ~/Text-to-PDF
git pull
```

Then launch it:

```bash
python3 text_to_pdf.py
```
