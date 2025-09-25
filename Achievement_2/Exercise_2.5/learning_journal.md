**Exercise 2.5: Django MVT Revisited**

**Learning Goals**

* Add images to the model and display them on the frontend of your application  
* Create complex views with access to the model  
* Display records with views and templates

**Reflection Questions**

1. **In your own words, explain Django static files and how Django handles them.**

In Django, **static files** don’t change dynamically when the web app is running. An instance of the static files are **images**, **JavaScript** or **CSS** **files**. Static files can be stored in a ‘static’ folder on project level or app level. And then they can be used inside templates by adding **{% load static %}** at the beginning (above the ***\<head\>*** tag) of the html file, and later inside ***\<body\>*** tag use **{% static ‘path/to/static/file’ %}** to link template and static file.

2. **Look up the following two Django packages on Django’s official documentation and/or other trusted sources. Write a brief description of each.**

| Package | Description |
| ----- | ----- |
| **ListView** | The **ListView** built-in Django package is needed to create a list of objects and display them in a template. First it has to be imported from **django.views.generic** inside [**views.py**](http://views.py) file. Then with this package we can create a class-based view by specifying the **model** we want to display and template (**template\_name**). Next we can use a **for loop** inside a template file to loop through **objact\_list** (that comes automatically from ListView) using Django’s template language: **{% for object in object\_list %}**…….**{% endfor %}** |
| **DetailView** | The **DetailView** package is another class-based view used for displaying a single object. Just like ListView, it has to be also imported in [views.py](http://views.py), and specify model and template. The main difference is that instead of passing a list of objects, **DetailView** provides just one object to the template. By default, this object is available in the template as **object**. The object’s fields can be directly accessed, for example: **{{ object.name }}** |

3. **You’re now more than halfway through Achievement 2\! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? You can use these notes to guide your next mentor call.** 

   The course is going well and I’m starting to feel a little bit more confident with Django. It’s really motivating to see my code come to life in the browser, even though users can for now just view the list and details of recipes. I’ve struggled a little with URL patterns, but I’m improving each time I debug and fix an error. Overall, I feel excited to keep building more features.