# Python Virtual Environment Guide

A virtual environment keeps project dependencies separate from the global Python installation on your machine.

## Create A Virtual Environment

From the project root:

```bash
python3 -m venv venv
```

This creates a `venv` directory. This project already ignores `venv/` in `.gitignore`, which is correct because virtual environments should not be committed.

## Activate The Virtual Environment

On Linux or macOS(You use mac):

```bash
source venv/bin/activate
```


When activated, your terminal prompt usually shows `(venv)`, dont forget you can use a diff name.

## Confirm Python And Pip

```bash
python --version
pip --version
```
If they're not installed, use AI and try to install it in your terminal, if you face issues you cant solve reach out.

Using `python -m pip` is recommended because it makes sure pip belongs to the active Python environment.

## Install A Package

Example:

```bash
pip install requests
```

## Save Installed Packages To requirements.txt

After installing libraries, save them:

```bash
pip freeze > requirements.txt
```

This writes the installed package versions into `requirements.txt`.

## Install Packages From requirements.txt

When someone else clones the project, or when you recreate your environment, install the same dependencies with:

```bash
pip install -r requirements.txt
```

## Deactivate The Virtual Environment

```bash
deactivate
```

This returns the terminal to your normal system Python environment.

## Typical Workflow

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python "First Class/arrays.py"
deactivate
```

If `requirements.txt` is empty(It is rn), the install command will finish without installing anything. That is fine for now because the Class 1 code only uses Python's standard library.
