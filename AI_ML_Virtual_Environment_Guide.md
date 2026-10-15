# Python AI/ML Environment Setup Guide (Windows)

This guide covers creating, activating, using, and removing a Python virtual environment, installing AI/ML libraries, and working with Jupyter Notebook or JupyterLab.

## 1. Check Python and pip

Open **Command Prompt** (`Win + R` → type `cmd` → Enter), then run:

```bat
python --version
python -m pip --version
```

If `python` is not recognized, try:

```bat
py --version
```

Use `py` instead of `python` in the commands below if that is how Python works on your computer.

## 2. Create a project folder

```bat
mkdir AI-ML
cd AI-ML
```

Download or copy your `requirements.txt` into this folder. Check the files in the current folder with:

```bat
dir
```

Expected structure:

```text
AI-ML/
└── requirements.txt
```

## 3. Create a virtual environment (venv)

Run this from inside your project folder:

```bat
python -m venv .venv
```

- `.venv` is the folder that contains this project's isolated Python environment.
- You normally create the environment only once per project.
- If you use `py`, run `py -m venv .venv`.

## 4. Activate the environment

### Windows Command Prompt (cmd)

```bat
.venv\Scripts\activate
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because scripts are disabled, you can use Command Prompt instead. Alternatively, for the current PowerShell session only, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

When activated, your prompt should begin with `(.venv)`.

## 5. Install or update packages

First, upgrade pip:

```bat
python -m pip install --upgrade pip
```

Install everything listed in `requirements.txt`:

```bat
python -m pip install -r requirements.txt
```

Install one extra package when needed:

```bat
python -m pip install package-name
```

Example:

```bat
python -m pip install requests
```

Check installed packages:

```bat
python -m pip list
```

Show details for one package:

```bat
python -m pip show numpy
```

Save the current environment's installed packages to a file:

```bat
python -m pip freeze > requirements-lock.txt
```

Install from that saved list later:

```bat
python -m pip install -r requirements-lock.txt
```

**Tip:** Run package-install commands while the correct `.venv` is activated.

## 6. Open Jupyter Notebook or JupyterLab

With `.venv` activated, install Jupyter if it is not already in your `requirements.txt`:

```bat
python -m pip install notebook jupyterlab ipykernel
```

Register this environment as a notebook kernel:

```bat
python -m ipykernel install --user --name ai-ml --display-name "Python (AI-ML)"
```

Start the classic Jupyter Notebook interface:

```bat
jupyter notebook
```

Or start JupyterLab:

```bat
jupyter lab
```

Jupyter normally opens in your web browser. In the interface, create a new notebook and select **Python (AI-ML)** if the kernel selector appears.

To stop the Jupyter server, return to the terminal where it is running and press `Ctrl + C`. Confirm if prompted.

If the `jupyter` command is not found, try:

```bat
python -m notebook
```

or:

```bat
python -m jupyterlab
```

## 7. Use the environment again later

Each time you open a new terminal, activate the environment again.

```bat
cd path\to\AI-ML
.venv\Scripts\activate
```

Replace `path\to\AI-ML` with the actual folder path. For example:

```bat
cd "%USERPROFILE%\AI-ML"
.venv\Scripts\activate
```

Then start Jupyter:

```bat
jupyter lab
```

## 8. Deactivate the environment

When you finish using the environment, run:

```bat
deactivate
```

This returns the terminal to your normal Python environment. It does **not** delete the virtual environment or uninstall its packages.

You do not need to deactivate before closing the terminal, but it is useful when switching projects.

## 9. Check which Python is running

While the environment is activated:

```bat
python --version
python -m pip --version
where python
```

The first Python path shown by `where python` should point to your project's `.venv\Scripts\python.exe`.

You can also check from Python:

```bat
python -c "import sys; print(sys.executable)"
```

## 10. Test common AI/ML libraries

Run this in the activated environment:

```bat
python -c "import numpy, pandas, sklearn, torch; print('Imports successful'); print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```

`CUDA available: False` does not mean PyTorch is broken. It may mean the computer has no supported NVIDIA GPU or the CUDA-compatible setup is not configured. CPU-based projects can still run.

## 11. Remove or rebuild an environment

To remove an environment, first stop Jupyter (`Ctrl + C`) and deactivate it:

```bat
deactivate
```

Then, from the project folder, delete the `.venv` directory:

```bat
rmdir /s /q .venv
```

**Warning:** This permanently removes that virtual environment and all packages installed inside it. It does not delete your project files or `requirements.txt`.

To recreate and reinstall:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 12. Troubleshooting

### `python` is not recognized

Try `py --version`. If that works, use `py` to create the environment:

```bat
py -m venv .venv
```

Otherwise, reinstall Python from the official Python website and enable the option to add Python to PATH.

### `pip` is not recognized

Use pip through Python:

```bat
python -m pip --version
python -m pip install package-name
```

### `requirements.txt` cannot be found

Check your current folder and its files:

```bat
cd
dir
```

Navigate to the folder containing `requirements.txt`, or use the full path to the file.

### A package fails to install

Check the Python version and the full error message:

```bat
python --version
python -m pip --version
```

Some packages may not yet support every Python version or operating system. Use a supported Python version for the packages you need and consult the package's official installation instructions.

### Jupyter opens with the wrong Python environment

In the notebook, choose **Kernel → Change Kernel → Python (AI-ML)**. If that option is missing, activate `.venv` and repeat the `ipykernel install` command in Section 6.

## 13. Quick command reference

| Task | Command (Command Prompt) |
|---|---|
| Check Python version | `python --version` |
| Create environment | `python -m venv .venv` |
| Activate environment | `.venv\Scripts\activate` |
| Deactivate environment | `deactivate` |
| Upgrade pip | `python -m pip install --upgrade pip` |
| Install requirements | `python -m pip install -r requirements.txt` |
| Install a package | `python -m pip install package-name` |
| List packages | `python -m pip list` |
| Save installed package versions | `python -m pip freeze > requirements-lock.txt` |
| Start Notebook | `jupyter notebook` |
| Start JupyterLab | `jupyter lab` |
| Stop Jupyter | `Ctrl + C` in the terminal running it |
| Show Python executable | `python -c "import sys; print(sys.executable)"` |

## Recommended daily workflow

```bat
cd "%USERPROFILE%\AI-ML"
.venv\Scripts\activate
jupyter lab
```

When finished, stop Jupyter with `Ctrl + C`, then run:

```bat
deactivate
```

Keep `.venv` local to your computer; do not upload it to GitHub. Keep `requirements.txt` in your project so the environment can be recreated later.
