# Troubleshooting Center

This folder collects fixes for setup and conversion problems.

## Start here

1. Run `python --version` (Windows) or `python3 --version` (Ubuntu/Linux).
2. Run the tool using the same Python command that you used to install ReportLab.
3. If you see an error, copy the complete error message—not just the last line.

## Guides

- [Ubuntu: No module named pip](UBUNTU_PYTHON_PIP.md)
- [Windows: Python, CMD, PATH, and Microsoft Store aliases](WINDOWS_PYTHON.md)
- [Common converter errors](COMMON_ERRORS.md)

## Important distinction: Windows vs Ubuntu

Windows Python and Ubuntu/WSL Python are separate installations. A package installed in one environment is not automatically available in the other. Use Windows commands in CMD/PowerShell and Linux commands in Ubuntu.

## Privacy and local file access

The interactive file picker lets you choose a file on your own computer. It does not upload your file. The tool only reads the file you select and writes the resulting PDF to the location you choose.
