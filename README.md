
# PixelPlay

An E-Commerce about Gaming Appliances created by Andriyo Averill Fahrezi with the ID of 2306172325.

Link to PWS : https://andriyo-averill-pixelplay.pbp.cs.ui.ac.id/

# Individual Assignment 2



#### -- How to Implement Everything in the Checklist --

a) Creating a new project in Django
- Start by creating a new directory named `PixelPlay`, this is the name of my E-Commerce.
- Create a *virtual environment* inside that directory with `python -m venv env` to simplify everything we will use in that environment (creating an isolated environment just for this application).
- Create a new Django project by executing `django-admin startproject PixelPlay`.
- Once the project is created, we move the directory to it with `cd PixelPlay`.
b) Configure routing on the project to run the main application
- Create an application named main in the project with `python manage.py startapp main`.
- Configure the application in settings, by adding the string "main" to the **settings.py** file located in the `PixelPlay` project directory in the _INSTALLED_APPS_ list.
c) Create a *Product* model in **models.py**
- In the `main/models.py` directory, create a Product model with the requested `name`, `price`, and `description` attributes.
d) Migrate the model to a Database
- Once the model is complete, migrate the model to the database, using `python manage.py makemigrations` and `python manage.py migrate`.
e) Creating a function in **views.py**
- Inside `main/views.py`, create a function that returns an HTML template.
f) Creating an HTML template
- Create a templates folder inside the *main* folder, then create an HTML file **main.html** inside it.
g) Configure routing in **urls.py**
- Create a **urls.py** file in the *main* folder, then add routing to map the functions from **views.py**.
- Also add routing in **urls.py** in the project folder to connect the main application.
h) Deploying to PWS Platform
- Log-in to the PWS page on https://pbp.cs.ui.ac.id
- Click on `Create new Project` with the Project Name of `PixelPlay`, then `Create new Project`
- Added my URL Deployment e.g. `andriyo-averill-PixelPlay.pbp.cs.ui.ac.id` in the _ALLOWED_HOST_ list on **settings.py** file 
- Run the command contained in the Project Command information on the PWS page
- Do `git push pws main:master` for future changes on the Django Project

#### -- Image Diagram --

![Notes_240910_213901](https://github.com/user-attachments/assets/1bd36e60-9cb5-4143-9812-6ce2e75fc5c2)

#### -- The Use of `git` in Software Development --

Git can help on large project assignments and collaboration between multiple developers to work on the same project at the same time. With Git, we can do `git branch` to create different features, and then we merge it back to the main project. We can also do `git clone` which we can do projects without having internet connection. Also, since we do `git push` into a repository, we don't have to worry about losing our code since we would always have a backup on our GitHub repository. Finally, since Git enables collaborators, when we do `git pull` requests, we can review our code before it's merged, ensuring a better quality and collaboration.

#### -- Why Django is Used as a Starting Point for Learning Software Development --

Personally, the reason behind Django is used for learning Software Development is because it is built-in on the easiest programming language, Python. What I have read online is Django is used for developing website such as Instagram, a daily app that I use, which would mean that it provides complete picture of web development. By seeing the template on the tutorial, Django can also be well documented with most of its library to install already having comments on them, that would provide a good resource for learning as a beginner.

#### -- Why is the Django model called an ORM? --

Django's model is called an ORM, Object-Relational Mapper, because it provides an abstract layer between the database and the Python code. In Django, when we define models as Python classes, these classes represent entities, with class attributes representing the fields of the database as seen in this code:
```bash
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
```