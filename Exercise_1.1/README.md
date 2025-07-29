# Exercise 1.1 - Getting Started with Python 

---

## Overview

**Exercise 1.1** is the first exersice of my Achievement 1 from the **Python for Web Developers** specialization CareerFoundry course.

This exercise covers the following tasks:

- Check if Python is already installed, if not install it (version 3.9.6)
- Install `virtualenvwrapper` package
- Created a virtual environment named `cf-python-base` using `virtualenvwrapper`
- Install IPython - similar to regular Python REPL but with additional features (such as syntax highlighting, auto-indentation and robust auto-complete features)
- Created a simple Python script `add.py` allowing users to:
  - enter two numbers
  - add them together
  - get the sum 
- Exported environment dependencies to `requirements.txt`
- Created a copy of the environment `cf-python-copy` using the same dependencies

---

## Project Structure

─> add.py  <br/>
─> requirements.txt (list of package requirements for this Python app)

---

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/tamperic/cf-python-course.git
cd cf-python-course
```

### 2. Create a virtual environment
```bash
mkvirtualenv cf-python-base
```

### 3. Activate a virtual environment
```bash
workon cf-python-base
```

### 4. Install dependencies (optional)
```bash
pip install -r requirements.txt
```

---

## Running the Script
- Make sure you are in the virtual environment:
```bash
workon cf-python-base
```

- Run the program:
```bash
python add.py
```

- Example:
```bash
Enter first number: 4
Enter second number: 3
4 + 3 = 7
```

---

## Exporting the Environment 
- If you want to export your current environment:
```bash
pip freeze > requirements.txt
```
- To replicate it in another virtual environment:
```bash
mkvirtualenv cf-python-copy
pip install -r requirements.txt
```