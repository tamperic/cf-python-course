# Learning journal

## Exercise 1.5: Object-Oriented Programming in Python

### Learning Goals

- Apply object-oriented programming concepts to your Recipe app

### Reflection Questions

1. **In your own words, what is object-oriented programming? What are the benefits of OOP?**

    **Object-oriented programming (OOP)** is a way of programming where code is organized into objects that combine data (data attributes) and behavior (procedural attributes - methods) and use them multiple times across the codebase to avoid repeated pieces of code. The main benefits of OOP include non-repeated and reusable code, reduced code duplication, easier to maintain, improved readability and organization. 

2. **What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.**

    A **class** in Python is an internal structure that defines how something should be structured and what it should do. It contains data _attributes_ (variables) and _methods_ (functions that define behavior). An **object** is a specific instance created from the class. While a class represents a general concept, the object represents one example of it. 
    For example:
    - A class could be `ClothingProduct`, with attributes such as `type`, `size`, `color`, and `brand`.
    - An object would be a clothing product created from that class: 
        - `ClothingProduct("Leggins", "M", "Gree", "Puma")`
        - Here the class is _ClothingProduct_, and the object is a _blue Puma legging in size M_.


3. **In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine.**

    - An OOP's method called **inheritance** means that one class can get properties and methods from another class. The class that gives is called the **parent class** and the class that receives is called **child** or **subclass**. The benefit of this method is avoiding repeating code and making it easier to maintain. For example, imagine a parent class called `Animal` with a `name` attribute and a `speak()` method. Both of these can be automatically inherited in subclasses like `Cat` and `Dog`. Each subclass still gets the attributes and methods from the parent, but it can also define its own behavior. In the `Cat` subclass, the name attribute could be `"Stripes"` and the `speak()` method could return `"Meow!"`. In the `Dog` subclass, the name might be `"Rex"` and the `speak()` method could return `"Woof!"`.
    - **Polymorphism** is a concept that allows different objects to use the same method name but do different things depending on the object. This makes code easier to read and use because the same method can be called on different objects without worrying about their specific type. For example, if there were two classes, `Dog` and `Cat`, and both have a method called `speak()`. The output of Dog would be `“Woof!”`, and the output of the Cat class would be `“Meow!”`. Even though we call `speak()` method the same way for every object, each object responds differently.
    - In Python, `==`, `*`,  `-` or `+`  operators usually work with built-in types - such as numbers or strings. But with **operator overloading** it can be defined how these operators work when used with custom objects. This can be done by implementing methods like:
        - `__add__` for `+`, 
        -  `__sub__` for `-`, 
        - `__mul__` for `*`,
        - `__eq__` for `==`,etc. 
    </br> 
    For example, imagine there is a class `ClothingSize` that represents shirt sizes measured in centimeters. It could be defined how two clothing sizes combine by writing the `__add__` method. Then, when the `+` operator is used with two `ClothingSize` objects, it will add their measurements and return a new `ClothingSize` object. 