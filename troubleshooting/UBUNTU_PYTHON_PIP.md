# Ubuntu: `No module named pip`

You may not need pip to install ReportLab on Ubuntu. Install the package with apt:

```bash
sudo apt update
sudo apt install -y python3-reportlab python3-venv
```

Verify:

```bash
python3 -c "import reportlab; print(reportlab.Version)"
```

Then run the converter with `python3 text_to_pdf.py notes.txt`.

## If you need pip in a virtual environment

```bash
sudo apt update
sudo apt install -y python3-full python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
python -m pip install reportlab
```

Use `python` inside the activated virtual environment. Do not use `sudo pip`. Modern Ubuntu may prevent pip from modifying system Python; use apt or a venv.

If pip is still missing, check:

```bash
which python3
python3 --version
ls -l .venv/bin/python*
```

Windows Python and Ubuntu/WSL Python are separate. Packages installed in one do not automatically work in the other.