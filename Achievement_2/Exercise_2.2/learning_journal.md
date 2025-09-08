# 2.2 Learning Journal 

## Exercise 2.2: Django Project Set Up

### Learning Goals

* Describe the basic structure of a Django project   
* Summarize the difference between projects and apps  
* Create a Django project and run it locally  
* Create a superuser for a Django web application

### Reflection Questions

1. **Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference.**   
   ***(Hint: In the Exercise, you saw the example of the CareerFoundry website in the Project and Apps section.)***

   For example, let’s analyze the website [***https://grandeturismo.com/***](https://grandeturismo.com/) . In Django terms:  
   * The whole ***`Grande Turismo`*** website would be a **project**.  
   * Inside this project, individual modules like login, explore, blog, can be considerate as **apps** \- each with a specific function.  
   * **Models** or data structure would represent data (for example, Event, Blog post, Category/Country, etc.)  
   * **Views** backend logic like fetcheing and displaying upcoming events.  
   * **Templates** frontend logic that handles the layout and design of the page.  
   * **URL routes** connect user requests to the view (/how-it-works, /blog, /log-in, etc.)  
2. **In your own words, describe the steps you would take to deploy a basic Django application locally on your system.** 

   To deploy a Django app locally, I would follow these steps:  
   1. First create a new or activate already created virtual environment.  
   2. Then with the activated virtual environment install Django by running this command: `pip install django`. And check if it’s properly installed by showing its version: `django-admin --version`.   
   3. In the next step I’d create a new Django project with the `django-admin startproject <nameofproject>` command.  
   4. Inside this newly created project (`cd <nameofproject>`) I’d also create apps: `python manage.py startapp <nameofapp>`.  
   5. Create a superuser account: `python manage.py createsuperuser -` then enter username, email and password.  
   6. With `python manage.py migrate` run database migrations.  
   7. Use `python manage.py runserver` to start the local development server and copy the link from the terminal and paste it in the browser to see the confirmation message that it’s successfully deployed.

3. **Do some research about the Django admin site and write down how you’d use it during your web application development.**  

   The Django admin site is a built-in feature that saves a lot of time during development. It allows me to perform CRUD operations (create, read, update, and delete) directly on my models without writing extra code. I can also use it to test models, manage user accounts, assign permissions, and even create groups, which makes collaboration easier for the whole team. It provides a practical and efficient way to manage both data and users while building an application.

