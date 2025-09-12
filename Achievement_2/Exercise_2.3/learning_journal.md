# 2.3 Learning Journal

## Exercise 2.3: Django Models

### Learning Goals

* Discuss Django models, the “M” part of Django’s MVT architecture  
* Create apps and models representing different parts of your web application   
* Write and run automated tests

### Reflection Questions

1. **Do some research on Django models. In your own words, write down how Django models work and what their benefits are.**

    In Django, the **M** in **MVT** stands for **Model**, which is a Python class used to interact with the database. Each attribute in the model class corresponds to a column in the database table. Once a developer defines a model, Django automatically translates it into SQL for the database. Thanks to Django’s **ORM (Object Relational Mapper)**, developers can then use Python code to create, edit, delete, or read rows from the database without having to write SQL manually.

    **Benefits of Django Models:**

    * No manual SQL required, Django handles the queries for developers.  
    * Adding or editing tables and fields is simpler.  
    * Built-in validation, like max length for text, etc.  
    * Models can be reused across views, templates, and forms, reducing duplication.  
    * Models plug automatically into Django’s admin panel, giving developers a quick way to manage data.

2. **In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer.**

    It is very important to write tests from the very beginning because it helps to continue building a project error free, especially as the project tends to grow. So if developer would wait and start doing tests later or at the end, it would be more messy, harder and even more expensive to fix those bugs. As an example we can use a **recipe web app** \- and one example of doing the test could be to check the recipe difficulty based on cooking time and number of ingredients. If the cooking time and/or number of ingredients change to check if the difficulty will be properly calculated.