# 2.4 Learning Journal 

## Exercise 2.4: Django View and Templates

### Learning Goals

* Summarize the process of creating views, templates, and URLs   
* Explain how the “V” and “T” parts of MVT architecture work  
* Create a frontend page for your web application

### Reflection Questions

1. **Do some research on Django views. In your own words, use an example to explain how Django views work.**

   As a first step it’s needed to create a file called `view.py` inside the app folder where we’re gonna write a view that represents a Python class or function for logic that handles requests and returns the response (such as HTML file, JSON data, image, etc.). Take a look at the following example:
      ```bash
      from django.shortcuts import render

      def home(request):

         return render(request, 'recipes/recipes\_home.html')
      ```

   In this example when user visits the home page, Django selects the view based on the URL from the web application in the browser, the `home` function inside view takes that web request and returns a web response which in this case is `recipe\_home.html` file.

2. **Imagine you’re working on a Django web development project, and you anticipate that you’ll have to reuse lots of code in various parts of the project. In this scenario, will you use Django function-based views or class-based views, and why?**

   In this case I would definitely use the CBV (class-based view), because they use Python classes. These classes can be defined just once and later can be reused across the project (several apps) as many times as needed. So in this way it prevents code duplicating and rewriting. 

3. **Read Django’s documentation on the [Django template language](https://docs.djangoproject.com/en/5.2/ref/templates/language/) and make some notes on its basics.**

   The **Django Template Language** is a built-in system in Django for writing dynamic HTML pages that allows combining static HTML and dynamic data from Django views.  The main constructs are variables and tags:

   - **Variables** are surrounded by **{{**.....**}}** and they get replaced with values.  
   - **Tags** are surrounded by **{%**....**%}** and they control the logic of the template. Tags are more complex than variables. The more used tags are: for, if, elif, else, block, extends.  
   - **Filters** use a pipe ( **I** ) and they modify the values of variables and tag arguments before displaying.  
   - **Comments** use the comment syntax **{\# \#}** to comment-out part of a line in a template.

