
# PixelPlay

An E-Commerce about Gaming Appliances created by Andriyo Averill Fahrezi with the ID of 2306172325.

Link to PWS : https://andriyo-averill-pixelplay.pbp.cs.ui.ac.id/

# Individual Assignment 2



#### -- How to Implement Everything in the Checklist --

1. Creating a new project in Django
- Start by creating a new directory named `PixelPlay`, this is the name of my E-Commerce.
- Create a *virtual environment* inside that directory with `python -m venv env` to simplify everything we will use in that environment (creating an isolated environment just for this application).
- Create a new Django project by executing `django-admin startproject PixelPlay`.
- Once the project is created, we move the directory to it with `cd PixelPlay`.
2.  Configure routing on the project to run the main application
- Create an application named main in the project with `python manage.py startapp main`.
- Configure the application in settings, by adding the string "main" to the **settings.py** file located in the `PixelPlay` project directory in the _INSTALLED_APPS_ list.
3. Create a *Product* model in **models.py**
- In the `main/models.py` directory, create a Product model with the requested `name`, `price`, and `description` attributes.
4. Migrate the model to a Database
- Once the model is complete, migrate the model to the database, using `python manage.py makemigrations` and `python manage.py migrate`.
5. Creating a function in **views.py**
- Inside `main/views.py`, create a function that returns an HTML template.
6. Creating an HTML template
- Create a templates folder inside the *main* folder, then create an HTML file **main.html** inside it.
7. Configure routing in **urls.py**
- Create a **urls.py** file in the *main* folder, then add routing to map the functions from **views.py**.
- Also add routing in **urls.py** in the project folder to connect the main application.
8. Deploying to PWS Platform
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


## Individual Assignment 3

#### Creating a Form Input

1. Create a file called `forms.py` in the `main` directory with contents as follow:
    ```bash
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'price', 'description', 'category', 'stock', 'rating']
    ```
2. Edit the `views.py` file in the `main` directory to add these import statements:
    ```bash
    from django.shortcuts import render, redirect 
    from main.forms import ProductForm
    from main.models import Product
    ```
3. Create a function to add the database entries inside `views.py` file in the `main` directory with contents as follow:
    ```bash
    def create_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
        else :
            form = ProductForm()

        context = {
            'form': form
        }

        return render(request, "create_product.html", context)
    ```
4. Change the `show_main` function inside the `views.py` file to handle the products as follow:
    ```bash
    def show_main(request):
        products = Product.objects.all()
        context = {
            'npm' : '2306172325',
            'name': 'Andriyo Averill Fahrezi',
            'class': 'KKI',
            'products': products
        }

        return render(request, "main.html", context)
    ```
5. Create a directory `templates` in the main directory and create an HTML file with the name base.html that acts as a skeleton for views. Fill in the file contents with:
    ```bash
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```
6. Add the folder `templates` by editing `settings.py` in the project directory e.g. `pixelplay` as follow:
    ```bash
    ... 
    {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
    ...
    ```
7. Implementing a database into the main page `main.html` so that it uses the `base.html` as the main templte and also `extends base.html` in the main directory
    ```bash
    {% extends 'base.html' %}
    {% block content %}
    <h1>Pixel Play</h1>

    <h5>NPM: </h5>
    <p>{{ npm }}<p>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>

    <h2>Our Gaming Products</h2>

    {% if not products %}
    <p>There are no gaming products available at the moment.</p>
    {% else %}
    <table>
    <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Category</th>
        <th>Stock</th>
    </tr>

    {% comment %} Looping melalui produk untuk menampilkannya di tabel {% endcomment %}
    {% for product in products %}
    <tr>
        <td>{{ product.name }}</td>
        <td>${{ product.price }}</td>
        <td>{{ product.description }}</td>
        <td>{{ product.category }}</td>
        <td>{{ product.stock }}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_product' %}">
    <button>Add New Product</button>
    </a>

    {% endblock content %}
    ```

#### Add 4 Views To The Added Objects 
Since we want to view by ID, we need to change the primary key to UUID as a way to make our application secure. Here&apos;s how!

1. On `models.py` in the `main` directory, add these lines as follow:
    ```bash
    import uuid # add this at the top (import statements)
    ...
    class ...
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        ...
    ```
Don&apos;t forget to do model migration since we are changing the `model.py`!

2. Add these imports to `views.py` file in the `main` directory at the top of the file
    ```bash
    from django.http import HttpResponse
    from django.core import serializers
    ```
3. We create a function inside `views.py` in the main directory to display JSON and XML as a whole and by ID per database entry
    ```bash 
    def show_xml(request):
        product = Product.objects.all()
        return HttpResponse(serializers.serialize('xml', product), content_type='application/xml')

    def show_json(request):
        product = Product.objects.all()
        return HttpResponse(serializers.serialize('json', product), content_type='application/json')

    def show_xml_by_id(request, id):
        product = Product.objects.get(pk=id)
        return HttpResponse(serializers.serialize('xml', product), content_type='application/xml')

    def show_json_by_id(request, id):
        product = Product.objects.get(pk=id)
        return HttpResponse(serializers.serialize('json', product), content_type='application/json')
    ```

#### Create URL Routing For All Function Inside `views.py`
1. Import all the function we made in `views.py` to `urls.py` file in the main directory at the top of the file as follow:
    ```bash 
    ...
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ...
    ```

2. Inside the `urls.py` file in the `main` directory add all the appopriate URL from the modification that we made to `views.py` as follow:
    ```bash
    ...
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product/', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    ]
    ...
    ```
3. Test the application on localhost with:
    ```bash
    python manage.py runserver
    ```
Then open http://localhost:8000/ on your _browser_

### Answers to the Questions
1. **Why we need data delivery in implementing a platform**

    The main reason of implementing a data delivery in a platform is to have end-to-end data driven approaches. Platforms need to interact with databases, users, and others (just like the diagram on Individual Assignment 2). These interactions require data to be moved 
    between different aspects of the system. By having data delivery we would ensure:

- User requests like forms are properly handled
- Data is synchronized across parts of system
- Reports with the database would run perfectly

2. **Which is better, XML or JSON? Why is JSON more popular?**

    In my opinion, JSON is better because by seeing the Postman response from getting the URL, it is much simpler and more readable than XML. The reason why JSON is more popular because of the advantage that I just said, especially in web development, where simplicity are crucial for handling large amounts of data.

3. **The fuctional usage of `is_valid()` method in Django forms**

    In Django, the `is_valid()` method checks if the data submitted through the form attaches to the validation defined in the form fields and to check whether the form has no errors. By using `is_valid()` we would ensure that:

- All the required fields of the forms are filled in
- Field types of the models are respected

    If the data is valid, then `is_valid()` would returns `True`, allowing the form data to be processed (in my case is to be saved to the database). Meanwhile, if it is invalid, it returns `False`, and maybe the form errors would be displayed to the user.

    We need this method to prevent invalid data from being processed, ensuring the integrity and security of our application.

4. **Why we need `csrf_token` in Django forms**

    Django has `csrf_token` or Cross-Site Request Forgery token) to protect forms from a CSRF attacks. A CSRF attack occur when a shady site tricks a user into submitting a request to another site where they are authenticated. Now without a CSRF token:

- Attackers can perform unauthorized actions disguising as users, such as submitting forms
- Data would be compromised along with security, leading to data theft or sysmtem compromise

    An attacker can leverage all those stuffs if we do not implement `csrf_token`. The `csrf_token` ensures that the form submissions are coming from the autheticated user by generating a unique token that is verified on both the cliend and server sides.

5. **How do I impelemt the checklist above step-by-step**

    Already answered on top of this section 🙏😁

### Screenshot Postman
1. **JSON**
![Screenshot 2024-09-13 144838](https://github.com/user-attachments/assets/bf397516-8722-44c7-9842-01a4f8296ca8)

2. **XML**
![Screenshot 2024-09-13 144823](https://github.com/user-attachments/assets/9bd07b21-75d6-4429-910e-6c5a0306714c)

3. **JSON by ID**
![Screenshot 2024-09-13 145708](https://github.com/user-attachments/assets/25915a24-9a85-43c6-897f-17fbe0604c9b)

4. **XML by ID**
![Screenshot 2024-09-13 145720](https://github.com/user-attachments/assets/887ef154-56e0-4b3b-ae9f-b363ccedddb5)


