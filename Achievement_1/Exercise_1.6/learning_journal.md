# Learning journal

## Exercise 1.5: Databases in Python

### Learning Goals

- Create a MySQL database for your Recipe app

### Reflection Questions

1. **What are databases and what are the advantages of using them?**

    Databases are where we store/collect our data, and there are a couple of advantages of using them, such as storing data in a well structured and organized way, then possibility to manipulate data - add new, delete, edit already added data, etc. Once added data can always and easily but securely be accessed by having to enter a password.

2. **List 3 data types that can be used in MySQL and describe them briefly:**

    Data types:
    1. `VARCHAR(n)` - strings with number of characters represented through `n` inside the parentheses `()`.
    2. `INT` - standard integer
    3. `FLOAT` - decimal numbers

3. **In what situations would SQLite be a better choice than MySQL?**

    If it’s needed to use simple databases and to store light data (like storing customer’s emails) or for testing databases without having to set up the whole installation,  than data can be stored in simple db files using, for instance, Python - in that case **SQLite** can be better choice than **MySQL**.

4. **Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?**

    **JavaScript**: </br>
        - Frontend web, backend, mobile and desktop apps </br>
        - Complex syntaxes </br>
        - Sometimes confusing rules, more symbols </br>
        - Not so easy to learn as Python </br>
        - Often allows code execution even with some issues </br>

    **Python**: </br>
        - Backend, data science </br>
        - Simple syntaxes </br>
        - Better readability, clean code </br>
        - Very beginner-friendly, easy for learning </br>
        - Doesn’t allow code execution if there is error

5. **Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?**

    One limitation of Python is that it’s used for frontend web or mobile app development, since other languages and frameworks are better suited for it. Another limitation is that Python tends to use more memory compared to some lower-level languages, which can be a problem in resource-limited environments. From my own experience as a beginner, I find using the Python shell very helpful for testing small pieces of code. However, when working with testing larger pieces of code, debugging in the shell can become frustrating, so I prefer in those cases writing and running scripts instead.
