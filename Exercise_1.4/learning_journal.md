# Learning journal

## Exercise 1.4: File Handling in Python

### Learning Goals

- Use files to store and retrieve data in Python

### Reflection Questions

1. **Why is file storage important when you’re using Python? What would happen if you didn’t store local files?**

    File storage is important for storing data permanently on hardware (our machine) that users input, so that data can't be lost. Because without possibility of file storage when script would stop running, all entered data would be lost. So this way all entered data is saved on a separate file and can be used again after the script stops running. All this is very important for further development of the app.

2. **In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why?**

    **Pickles** are files that store complex Python data (such as dictionaries, lists)  in a binary format that is not readable for humans. **Pickling** is the process of converting Python objects into this binary format for storage, while **unpickling** is the process of converting the binary data back into Python objects.
    There is pickle module, that has to be imported and that provides two main methods for working with pickle files:
    1. `pickle.dump()` method for converting and storing data as bytes. The filename where the data is going to be stored should be inside the parenthesis `()` of this method as an argument.
    2. `pickle.load()` method which can be used to load the stored data from that file, and again the filename should be an argument. 


3. **In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?**

    I’d use the `os` module, where to find out in which directory am I currently using I would use the `os.getcwd()` command, and to change the directory `os.chdir()` command.

4. **Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?**

    In such a situation, I would use the **try-except** block. The `try` block contains instructions that can cause an error, and the `except` block solves it by displaying an appropriate error message or taking certain action. This way the script continues running without stopping due to an error.

5. **You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.**

    The Python course is going well so far. I’ve been going through the theory and learning the basics of Python, which makes me even more interested in continuing to learn. I haven’t faced any major issues with the tasks — just a few small problems that happened when I didn’t follow the instructions closely at first. However, rereading the instructions and reviewing the theory again has helped me solve them.
