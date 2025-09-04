# Exercise 1.2 - Data Types in Python 

## Overview

**Exercise 1.2** is the second exercise of my Achievement 1 from the **Python for Web Developers** specialization CareerFoundry course, which focuses on different variables and data types in Python.

This exercise covers the following tasks:

- Create the Exercise_1.2 folder and then navigate to it
- Activate the virtual environment by running `workon cf-pyhton-base` 
- Launch IPython shell by running `ipython`
- Create `recipe_1` structure as dictionary containing the following keys:
    - `name` (string),
    - `cooking_time` (integer),
    - `ingredients`(list of strings).
- Create `all_recipes` list containing recipe_1 (and later all other recipe dictionaries), 
- Create 4 more recipe dictionaries:
    - `recipe_2`,
    - `recipe_3`,
    - `recipe_4`,
    - `recipe_5`.
- Add them to the `all_recipes` list by running `all_recipes.extend()` method

---

## Project Structure

- Exercise_1.1 (folder containing the following files:) <br/>
  - add.py  <br/>
  - requirements.txt (list of package requirements for this Python app)
  - learning_journal.md
  - README.md
  - 1.1_Screenshots (folder containing png screnshots of each step from 1.1 Exercise)

- Exercise_1.2 (folder containing the following files:) <br/>
  - learning_journal.md
  - README.md
  - 1.2_Screenshots (folder containing png screenshots of each step from 1.2 Exercise)

---

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/tamperic/cf-python-course.git
cd cf-python-course
cd Exercise_1.2
```

### 2. Activate a virtual environment
```bash
workon cf-python-base
```

### 3. Launch IPython shell by running
```bash
ipython
```

### 4. Creating recipe structures - example:
```bash
recipe_1 = {
  "name": "Tea",
  "cooking_time": 5,
  "ingredients": ["Tea leaves", "Sugar", "Water"]
}

all_recipes = [recipe_1]
```

---

## Explanation - Why These Data Structures?
- A dictionary (`dict`) for single recipe is an ideal choice bacause it allows storing a different data types with meaningful keys and modifying the structure. In this exercise, for example, key `name` stores a string, `cooking_time` stores an integer, and `ingredients` stores a list of strings.
- A list (`list`) used for `all_recipes` allows storing a multiple recipe dictionaries and it can be manipulated after the list is created - added, changed, or deleted as needed.