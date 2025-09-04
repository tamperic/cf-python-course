# Learning journal

## Exercise 1.2: Data Types in Python

### Learning Goals

Explain variables and data types in Python <br/>
Summarize the use of objects in Python <br/>
Create a data structure for your Recipe app

### Reflection Questions

1. **Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?**

    **IPython** shell offers much better user experience for developers, like auto-indentation, syntax highlighting with colored text, auto-completion, which provides better code readability compared to **Python's default shell**. Whereby **default Python shell** doesn't provide such a good user experience - the same text color leads to a difficult code reading and writing, and code indentation has to be done manually, there is no auto suggestion for completing the code writing. All these features in **IPython** help in testing and debugging by providing a colorful feedback or error message immediately after running a command, making debugging easier and more efficient. In contrast, in the **default Python shell** it is more difficult to spot an error.

2. **Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.**

    | Data Type |                                 Definition                                  | Scalar or Non-Scalar? |
    |-----------|-----------------------------------------------------------------------------|-----------------------|
    |    int    |               defines whole numbers (e.g., 30, 5, -6)                       |         scalar        |
    |    str    | defines string of different characters - letters & numbers (e.g., “Welcome”)|       non-scalar      |
    |    list   |                  defines decimals (e.g., 4.5, -5.5)                         |       non-scalar      |
    |    bool   |               defines boolean - _*true*_ or _*false*_ statements            |         scalar        |
 


3. **A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.**

    **Lists** and **tuples** both define linear arrays and they can store a multiple data types, but the main difference between them is that **lists** are mutable - can change their values or delete, and **tuples** are immutable - can't change their values. So it means that **lists** should be used when data may change, and **tuples** when data stays constant. **Lists** as arrays use square brackets `[]`, and **tuples** use parentheses `()`.

4. **In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.**

    For such an app I would choose a dictionary as a suitable form of storing data by using the following keys: 
    - `word`, 
    - `category`, 
    - `definition`.
    
    Each key should contain a string, or `definition` key could be a list of strings if the word has multiple meanings as in this example:
    ```bash
    flashcard_1 = {
        "word": "deduction",
        "category": "noun",
        "definition":  "the action of deducting or subtracting something”
    }
    ```
    
    I think this is the most suitable choice because dictionaries offer a clear and mutable data structure that can be modified, especially if over time the app would grow - for instance adding new keys. 
    And each flashcard I would store as a list named `all_flashcards`, because compared to tuples, lists are mutable allowing the elements (flashcards) to be expanded, removed, or changed. 