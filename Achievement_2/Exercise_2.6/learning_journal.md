# 2.6 Learning Journal

## Exercise 2.6: User Authentication in Django

### Learning Goals

* Create authentication for your web application  
* Use GET and POST methods   
* Password protect your web application’s views

### Reflection Questions

1. **In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer.** 

    **Authentication** is an essential process that allows users to create and manage their own accounts, providing a personalized experience. It ensures that no one can access someone else’s account, keeping user data and privacy secure.

2. In your own words, explain the steps you should take to create a login for your Django web application. 

    To create a login for a Django web application, you generally follow these steps:

    * **Create login\_view** \- on project-level create a view file ([views.py](http://views.py)) and define a function-based view that handles user authentication. Here logout\_view can also be created.  
    * **Create template (login.html)** \- design the structure of the login page with a form allowing users to enter their credentials (username, password).   
    * **Specify URL mapping** \- this step can in this case be skipped because it is usually done inside [urls.py](http://urls.py) at the app level. But login should be created on project-level, so we can go directly to the project’s [urls.py](http://urls.py) and so to the next step.  
    * **Register URL to the project** \- first import the login\_view inside [urls.py](http://urls.py) at the project level and then define the login route (login\_view path) so that the login page can be accessible.  
3. Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each.

    | Function | Description |
    | :---- | :---- |
    | **authenticate()** | Authenticate() function’s purpose is to verify a set of user’s credentials (username, password). So it can take these credentials as keyword arguments, check them in the backend, and if they are valid returns a ‘User’ object. Otherwise, it returns None. <br> Syntax: <br> **from django.contrib.auth import authenticate <br> user \= authenticate (username=username, password=password) <br> if user is not None: <br>        \# Valid credentials \- a backend authenticated credentials <br> else: <br>        \# Invalid credentials \- no backend authenticated credentials** |
    | **redirect()** | We use this function to redirect user to another URL. This function can be used by passing an object as its argument, by passing the name of the view, or hardcoded or the full URL to redirect to. It returns an HttpResponseRedirect or HttpResponsePermanentRedirect  It’s commonly used to redirect user after form submission and successful login. <br> Example:  <br> **from django.shortcuts import redirect <br> return redirect(‘home’)** |
    | **include()** | This function allows us to include a template inside the current template. It is useful when we have the same block of content used across multiple pages.  <br> Syntax: <br> **{% include ‘template\_name.html’ %}** |

