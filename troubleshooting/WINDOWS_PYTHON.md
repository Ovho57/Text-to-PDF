# Windows: Python won't run in CMD

## Check what Windows finds

```cmd
where python
where py
python --version
py --version
```

If `where python` points to `%LOCALAPPDATA%\\Microsoft\\WindowsApps\\python.exe`, Windows may be using the Microsoft Store execution alias rather than the actual Python install.

## App execution aliases

Search Windows Settings for **App execution aliases**. If the `python.exe` and `python3.exe` aliases are causing the Store shortcut to launch, turn them off. Settings labels can vary by Windows version.

## Repair/install Python

Download only from https://www.python.org/downloads/windows/ . During setup, enable **Add Python to PATH** if offered and ensure pip is selected. Close and reopen CMD after setup.

```cmd
python --version
python -m pip --version
python -m pip install reportlab
```

If the Python launcher works, use `py` instead of `python`.

**Windows and Ubuntu are different environments.** Python installed in Ubuntu/WSL does not become available in Windows CMD, and vice versa.