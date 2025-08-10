# Learning journal

## Exercise 1.2: Data Types in Python

### Learning Goals

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

## Reflection Questions

1. **In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:**
- **The script should ask the user where they want to travel.**
- **The user’s input should be checked for 3 different travel destinations that you define.**
- **If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”**
- **If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”**
	
    ### Way 1:

    ```bash
    destination = input('Where do you want to travel?')

    if destination == 'Krakow' or destination == 'krakow':
        print('Enjoy your stay in Krakow!')
    elif destination == 'Tbilisi' or destination ==  'tbilisi':
        print('Enjoy your stay in Tbilisi')
    elif destination == 'Seville' or destination ==  'seville':
        print('Enjoy your stay in Seville')
    else:
        print('Oops, that destination is not currently available.')
    ```

    ### Way 2:

    ```bash
    destinations = ['Krakow', 'Seville', 'Tbilisi']

    question = input('Where do you want to travel?')

    if question in destinations:
        print('Enjoy your stay in', question, '!')
    else:
        print('Oops, that destination is not currently available.')
    ```

2. **Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.**

    Boolean logic operators are AND, OR and NOT, in Python used in lowercase. AND/OR operators can be used, for example, with an if-elif statement when you want to compare two or more conditions at the same time, or other cases.
    The logic operator AND should be used when you want to check if multiple conditions are met. The logic operator OR should be used when you want  to check if one of the multiple conditions is met. And the NOT operator is used to check if one condition was not met.

    `true and true` <br/>
    `false or true` <br/>
    `not false`

3. **What are functions in Python? When and why are they useful?**

    Functions in Python represent instructions that allow us to do certain actions. They can be once at the beginning of the code defined using keyword `def`, name of the function and optionally arguments inside parenthesis `()`. So the same logic written inside one certain function can be reused across the code multiple times. It doesn’t have to be rewritten, once declared can be just called later using the name of that function, which is very practical and easier to use.

4. **In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course.  In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.**

    I am starting to learn theory basics in Python like functions, different operators, variables, if-elif-else statements, etc. - which are similar to those in JS one, but with certain differences, and practice this through small tasks.
