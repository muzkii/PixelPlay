
# PixelPlay

An E-Commerce about Gaming Appliances created by Andriyo Averill Fahrezi with the ID of 2306172325.

Link to PWS : https://andriyo-averill-pixelplay.pbp.cs.ui.ac.id/

## Individual Assignment 2



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
5. Create a directory `templates` in the main directory and create an HTML file with the name `base.html` that acts as a skeleton for views. Fill in the file contents with:
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
7. Implementing a database into the main page `main.html` so that it uses the `base.html` as the main template and also `extends base.html` in the main directory
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
        return HttpResponse(serializers.serialize('xml', [product]), content_type='application/xml')

    def show_json_by_id(request, id):
        product = Product.objects.get(pk=id)
        return HttpResponse(serializers.serialize('json', [product]), content_type='application/json')
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

5. **How do I implement the checklist above step-by-step**

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

## Individual Assignment 4

#### Implement Register, Login, and Logout Functions

##### **Register**

1. In order to implement a register function, we have to make a function to create the user itself. Luckily, we can use the built-in function `UserCreationForm` inside Django. Add these imports in `views.py` in the `main` directory as follows:
    ```bash
    ...
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```

2. We can implement a register function and add to `views.py` as follows:
    ```bash
    def register(request):
        form = UserCreationForm()
    
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your new account has been sucessfully added!')
                return redirect('main:login')
        context = {
            'form':form
            }
        return render(request, 'register.html', context)
    ```
    As you can see, we would create the account when is_valid() is True (recall on assignment 2). It would redirect back to the login page for users to continue, as for now we haven't made the `login.html` page.

3. Following the step before, we have to create a new HTML file named `register.html` to render the register function as explained before in the `templates` subdirectory inside the main `directory` as follows:  
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}

    <div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Register" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}
    ```
4. Now don't forget to implement it into the `urlpatters` to access the function. On `urls.py` inside the `main` directory, import the function as follows:
    ```bash
    from main.views import ..., register
    ```
    Continue to add the URL path:
    ```
    urlpatterns = [
        ...
        path('register/', register name='register')
        ]
    ```

##### **Login**

5. In order to implement a login function, we can use the built-in function `authenticate`, `login`, and `AuthenticationForm` inside Django. Add these imports in `views.py` in the `main` directory as follows:
    ```bash
    ...
    from django.contrib.auth.forms import ..., AuthenticationForm
    from django.contrib.auth import authenticate, login
    ```

6. We can implement a login function and add to `views.py` as follows:
    ```bash
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
    
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    
        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```

7. Following the step before, we have to create a new HTML file named `login.html` to render the login function as explained before in the `templates` subdirectory inside the main `directory` as follows:  
    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```

8. Implement it into the `urlpatters` to access the function. On `urls.py` inside the `main` directory, import the function as follows:
    ```bash
    from main.views import ..., login_user
    ```

    Continue to add the URL path:
    ```
    urlpatterns = [
        ...
        path('login/', login_user, name='login')
        ]
    ```

##### **Logout**

9. In order to implement a logout function, we can use the built-in function `logout` inside Django. Add this import in `views.py` in the `main` directory as follows:
    ```bash
    ...
    from django.contrib.auth import ..., logout
    ```

10. We can implement a logout function and add to `views.py` as follows:
    ```bash
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

11. Following the step before, we have to add a button to the `main.html` file to act as the hyperlink tag to logout. We add the code in the `templates` subdirectory inside the main `directory` as follows:  
    ```bash
    ...
    <a href="{% url 'main:logout' %}">
        <button>Logout</button>
    </a>
    ```

12. Implement it into the `urlpatters` to access the function. On `urls.py` inside the `main` directory, import the function as follows:
    
    ```bash
    from main.views import ..., logout_user
    ```

    Continue to add the URL path:
    ```bash
    urlpatterns = [
        ...
        path('logout/', logout_user, name='logout')
        ]
    ```

    Now we have implemented all the functions as requested.

#### Display Logged-In User Details (Username) and Apply Cookies (Last Login)

##### **Implementing Cookies**

1. To implement last login, we need to have the date and time itself and to redirect after the form submission or other actions that we have did. We can use built-in Django function and Python function and import them to `views.py` on the `main` directory as follows:
    ```bash
    ...
    from django.http import ..., HttpResponseRedirect
    from django.urls import reverse
    import datetime
    ```

2. We can replace the previous line of code in `login_user` function inside `views.py` on the `main` directory from:
    ```bash
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('main:show_main')
    ...
    ```
    To:
    ```bash
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```

3. Now, we have to change the `show_main` function, inside the same file (`views.py` on the `main` directory) to handle last login in the `context` variable as follows:
    ```bash
    ...
    context = {
        'name': "andriyo averill",
        'products': products,
        'last_login': request.COOKIES.get('last_login')
    }
    ```

4. We have to also modify the `logout_user` function to be able to cookies based on when the user logged out as follows:
    ```bash
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

5. Lastly, we have to display the last login in `main.html` file on the `templates` subdirectory inside `main` directory, in order to do so we have to add the following:
    ```bash
    ...
    <h5>Last login session: {{ last_login }}</h5>
    ...
    ```

##### **Implementing Logged-In User**

6. We can implement it by editing `show_main` function inside `views.py` on the `main` directory. We have to change the code to as shown:
    ```bash
    ...
    context = {
        'name': request.user.username,
        'products': products,
    ...
    }
    ```

7. Since we have implemented a login function, it's best if secure it to make users have to login first before they can continue. To do this we can use a built-in Django function called `login_required`, we add this import to our `views.py` file in the `main` directory as follows:

    ```bash
    ...
    from django.contrib.auth.decorators import login_required
    ```

    Add this to `show_main`

    ```bash
    ...
    @login_required(login_url='/login')
    def show_main(request):
        ...
    ```

#### Two Accounts with Three *Dummy Data* Each Example

1. Account with the name of andriyo with the data as follows:

    ![Screenshot 2024-09-21 005104](https://github.com/user-attachments/assets/eadae369-5b1a-413e-8dd7-3b4711ecb5f4)

2. Account with the name of adyo with the three last data as follows:

    ![Screenshot 2024-09-21 005827](https://github.com/user-attachments/assets/7e587432-7725-422e-9a7c-d6d7e85ccd1e)

    Because we haven't connect the models where each user would have their own data, here we see that the data is still linked even though we are using different accounts.

#### Connect the Models `Product` and `User`

We need to create a relationship between the two models. Specifically, this involves establishing a database relationship so that instances of Product are linked to instances of User. There are several types of relationships, depending on how the models should interact with each other. Since I am taking Databases course, we can use ForeignKey (One to Many Relationship) as follows:

1. On `models.py` in the `main` directory we need to differentiate users, in that case we need to import the User itself as follows:
    ```bash
    ...
    from django.contrib.auth.models import User
    ```

2. We need to add the user itself to the models as follows, because we have `Product` model:
    ```bash
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
    Now we have bonded our `Product` model to a `User` through a ForeignKey relationship

    
3. Next, we have to edit our form function to be able to save the form based on the user. On `views.py` in the `main` directory modify `create_product` function as follows:
    ```bash
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == 'POST':
            products = form.save(commit=False)
            products.user = request.user
            products.save()
            return redirect('main:show_main')

        context = {
            'form': form
        }

        return render(request, "create_product.html", context)

4. Now, we have to filter all objects to only retrieve the `Product` where the `user` field is filled with the corresponding User as follows:
    ```
    def show_main(request):
        products = Product.objects.filter(user=request.user)
        context = {
            'name': request.user.username,
            'products': products,
            ...
    ```

5. Since we have made changes to `models.py` we have to run the model migration with:
    ```bash
    python manage.py makemigrations
    ```

6. Now select the default value for the `user` field based on the forms that we have already created earlier in the *dummy* account database.
    ```bash
    It is impossible to add a non-nullable field 'user' to product without specifying a default. This is because the database needs something to populate existing rows.
    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit and manually define a default value in models.py.
    Select an option: 1
    Please enter the default value as valid Python.
    The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
    Type 'exit' to exit this prompt
    >>> 1
    ```
    Now run:
    ```bash
    python manage.py migrate
    ```

7. Finally we have to make it such that our project is ready for a production environtment. Add these imports to `settings.py` on our project directory and the following:

    ```bash
    ...
    import os
    ```

    Then change the DEBUG in `settings.py` as follows:

    ```bash
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```

### Answers to the Questions

1. **What is difference between `HttpResponseRedirect()` and `redirect()`?**

    Since both has "Redirect" in their names so it must be to perform redirection, but they are used slightly differently. `HttpResponseRedirect` requires to explicitly provide the URL or use reverse() to look the URL up, meanwhile `redirect` is a more convenient shortcut that can automatically resolve a URL from a view name or model object just how we did in `logout_user` function.

2. **How the `MoodEntry` model is linked with `User`**

    Just like how I implemented in the top, so that each entry is associated with a specific user, we can implement to link it with ForeignKey relationship. This allows one user to have many mood entries, but eaach mood entry is associated with only one user, a One-To-Many relationship.

3. **Difference between *authentication* and *authorization* and what happens when a user logs in? Explain how Django implements these two concepts.**

    Authentication refers to verify (authenticate) who the user is. It checks from credentials usually provided in the form of username and password that is created by the user against stored credentials to confirm their own identity. In Django, authentication is handled through Django's built-in functions such as `authenticate()` and `login()` like:
    ```bash
    from django.contrib.auth import authenticate, login

    def user_login(request):
        user = authenticate(username='john', password='secret')
        if user is not None:
            login(request, user)
    ```

    Meanwhile, authorization refers to what action a user is allowed to do. It checks whether an authenticated user has certain permission to access certain resources or perform certain actions. In Django, authorization is handled by decorators like `@login_required` and `@permission_required` like:
    ```bash
    from django.contrib.auth.decorators import login_required

    @login_required
    def my_view(request):
        ...
    ```

    When a User logs in, Django sequentially do:
    
    - Authenticates: Checks the user's credentials (by `authenticate()`)
    - Creates session: When authentication is successful, Django creates a session for the user and stores the session ID in the browser's cookies (checked by inspecting and check the application)
    - Associates the session with the user: Django can keeps track of the user's aunthentication status through the session. Considered as "logged in" as long as the session is running

4. **How does Django remember logged-in users? Explain other uses of *cookies* and whether all cookies are safe to use.**

    Django uses **sessions** and **cookies** to remember looged-in users:

    - **Sessions**: Django stores session data (including whether a user is logged in) on the server side and associates it with a unique session ID. This session ID is sent to the user's browser as a cookie.
    - **Cookies**: A small file stored on the client’s machine. The session ID is stored in a cookie (sessionid by default), which is sent with each subsequent request. Django uses this cookie to retrieve the session data and confirm that the user is logged in.

    Other Uses of Cookies:

    - **Storing preferences**: Cookies can be used to store user preferences, such as language settings or theme choices, across sessions.
    - **Tracking activity**: Websites may use cookies to track user behavior for analytics or personalization purposes.
    - **Remembering form inputs**: Cookies can be used to prefill form fields with values entered previously by the user.

    Are All Cookies Safe to Use?
    Not all cookies are inherently safe. Here are some security considerations:

    - **Secure flag**: Cookies with the "Secure" flag are only sent over HTTPS, making them less vulnerable to interception.
    - **HttpOnly flag**: Cookies with the "HttpOnly" flag cannot be accessed by client-side JavaScript, preventing them from being exploited by cross-site scripting (XSS) attacks.
    - **Session Hijacking**: If a session cookie is intercepted, an attacker can impersonate the user.

5. **How do I impelemt the checklist above step-by-step**

    Already answered on top of this section 🙏😁


##  Individual Assignment 5

Before we can implement any functions on our Project, in my case, we have to add Tailwind to our app inorder to help us on styling our app. We can do so as follows:

1. Open Django project, in my case **PixelPlay**, open the `base.html` file on `/templates` folder on our root project.

2. Add the Tailwind cdn script in the head section as follows:

    ```bash
    ...
    {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
    </head>
    ```

### Implement New Functions 

#### Implement Functions to Delete Products

1. Open `views.py` file in the `main` folder, create a new function called `delete_product` that takes `request` and `id` as parameters. Edit as follows:

    ```bash
    def delete_product(request, id):
        product = Product.objects.get(pk=id) # Here is to get the product based on the id that we have made on the previous assignment
        product.delete() 
        return HttpResponseRedirect(reverse('main:show_main')) # Return to the home page
    ```

2. Don't forget to import the function by open `urls.py` in the `main` folder
as follows:

    ```bash
    from main.views import ..., delete_mood
    ```

3. Now we have to add the URL path to `urlpatterns` to access the imported function as follows:

    ```bash
        ...
        path('delete-product/<uuid:id>', delete_product, name='delete_product') # Don't forget to change the "id" data type, adjust it to match the data type on our models.py file
        ...
    ```

4. Next is to open the `main.html` file in the `main/templates` folder and modify our existing code to implement a delete button for each product as follows:

    ```bash
    ...
    <tr>
        ...
        <td>
            <a href="{% url 'main:delete_product' product.pk %}">
                <button>
                    Delete
                </button>
            </a>
        </td>
    </tr>
    ...
    ```

#### Implement Functions to Edit Products

1. Open `views.py` in the `main` directory, and create a new function named `edit_product` that takes `request` and `id` parameters as follows:

    ```bash
    def edit_product(request, id):
        # Get mood entry based on id
        product = Product.objects.get(pk = id)

        # Set product entry as an instance of the form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Save form and return to home page
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)
    ```

2. Now create a new HTML file named `edit_product.html` in the `main/templates` directory. Fill in the file with the following code:

    ```bash
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    <h1>Edit Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

3. Don't forget to import the function by open `urls.py` in the `main` folder
as follows:

    ```bash
    from main.views import ..., edit_product
    ```

4. Now we have to add the URL path to `urlpatterns` to access the imported function as follows:

    ```bash
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product') # Don't forget to change the "id" data type, adjust it to match the data type on our models.py file
    ...
    ```

5. Next is to open the `main.html` file in the `main/templates` folder and modify our existing code to implement a delete button for each product as follows:

    ```bash
    ...
    <tr>
        ...
        <td>
            <a href="{% url 'main:delete_product' product.pk %}">
                <button>
                    Delete Product
                </button>
            </a>
        </td>
        <td>
            <a href="{% url 'main:edit_product' product.pk %}">
                <button>
                    Edit Product
                </button>
            </a>
        </td>
    </tr>
    ...
    ```

### Customize the *template* HTML Using Tailwind and External CSS

Before we continue, it's important that since we are deploying our project to a web server, we have to add these imports and snippets to help us achieve having a static files. Static files are files that don’t change, thus, the server just fetches them
from the disk making it efficient and easier to cache. To do so as follows:

1. Open `settings.py` file in our project directory, in my case it's `PixelPlay`, then add *middleware* WhiteNoise like:

    ```bash
    ...
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    ]
    ...
    ```
    
    Here, WhiteNoise serves to run the static file automatically without having to configure anything.

2. Make sure that `STATIC_ROOT`, `STATICFILES_DIRS`, and `STATIC_URL` are configure as follows:

    ```bash
    ...
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static' 
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static' 
    ...
    ```

3. Since here I am using Tailwind and External CSS, we have to modify some code on our `base.html` file to accepts External CSS (since we have did Tailwind at the start, creating the external css file is on the next step) as follows:

    ```bash
    ...
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
    </head>
    ...
    ```

4. Now create a new directory on the `root` of our project called `static` and inside that directory, create a new subdirectory called `css`. It should be Now inside the `css` directory, create a file called `global.css`. At the end it should look like `static/css/global.css`. Now modify the `global.css` file that servers as a *custom styling* that I have made as follows:
    ```bash
    .form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #4a4a4a; 
    border-radius: 0.5rem; 
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); 
    }

    .form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #4a90e2;
    background-color: #f0f8ff;
    box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.5);
    }

    @keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
    }

    .animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 2s infinite; 
    }
    ```

    Now we can move on to styling our pages

#### Customizing Login Page

Open the `login.html` file and change the code as follows:

    ```bash
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center w-screen bg-gradient-to-r from-orange-400 to-teal-400 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full bg-white shadow-lg rounded-lg p-8 space-y-8">
        <h2 class="mt-6 text-center text-gray-800 text-3xl font-bold">
        Welcome Back
        </h2>
        <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
            <label for="username" class="sr-only">Username</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-lg relative block w-full px-4 py-3 mb-4 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent" placeholder="Username">
            </div>
            <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-lg relative block w-full px-4 py-3 mb-4 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent" placeholder="Password">
            </div>
        </div>
        

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500">
            Log In
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
            {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
            {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
            {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
            {% endif %}
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-gray-600">
            Don't have an account?
            <a href="{% url 'main:register' %}" class="font-medium text-orange-600 hover:text-orange-500">
            Sign Up Here
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```

#### Customizing Register Page

Open the `login.html` file and change the code as follows:

    ```bash

    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center bg-teal-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
        <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-teal-700">
            Create your account
        </h2>
        </div>
        <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
                </label>
                <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    {% endif %}
                </div>
                </div>
                {% if field.errors %}
                {% for error in field.errors %}
                    <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
                {% endif %}
            </div>
            {% endfor %}
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
            Register
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
        <div class="bg-orange-100 border border-orange-400 text-orange-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-black">
            Already have an account?
            <a href="{% url 'main:login' %}" class="font-medium text-orange-600 hover:text-orange-700">
            Login here
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```

#### Creating Navigation Bar 

Before we can continue to customize our add product page, we have to create a navigation bar since cuztomizing the add product page would means that we need the navigation bar itself first, here's how to implement it:

1. Open the `templates/` folder in the `root` directory, the same directory that we have our `base.html` file, and create a new file called `navbar.html` with contents as follows:

    ```bash
    <nav class="bg-teal-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center">
                    <h1 class="text-xl font-bold text-center text-green-50 tracking-widest">
                        P I X E L &nbsp; P L A Y
                    </h1>
                    
                </div>
                <div class="hidden md:flex items-center space-x-4">
                    <!-- Links with hover effects -->
                    <span class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Home</span>
                    <span class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Products</span>
                    <span class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Categories</span>
                    <span class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Cart</span>

                    {% if user.is_authenticated %}
                    <span class="text-white font-bold py-2 px-4 rounded-lg">
                        Welcome, {{ user.username }}
                    </span>                                
                        <a href="{% url 'main:logout' %}" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                            Logout
                        </a>
                    {% else %}
                        <a href="{% url 'main:login' %}" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mr-2">
                            Login
                        </a>
                        <a href="{% url 'main:register' %}" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                            Register
                        </a>
                    {% endif %}
                </div>
                <div class="md:hidden flex items-center">
                    <button class="mobile-menu-button">
                        <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile menu -->
        <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
            <div class="pt-2 pb-3 space-y-1 mx-auto">
                <!-- Mobile links with hover effects -->
                <span class="block bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Home</span>
                <span class="block bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Products</span>
                <span class="block bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Categories</span>
                <span class="block bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">Cart</span>

                {% if user.is_authenticated %}
                <span class="text-white font-bold py-2 px-4 rounded-lg">
                    Welcome, {{ user.username }}
                </span>              
                    <a href="{% url 'main:logout' %}" class="block bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                        Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="block bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mb-2">
                        Login
                    </a>
                    <a href="{% url 'main:register' %}" class="block bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                        Register
                    </a>
                {% endif %}
            </div>
        </div>
        <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
        
        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
        </script>
    </nav>
    ```

    Here, we would have a responsive navigation bar for both desktop and mobile versions.

2. Now, don't forget to link the navigation bar to `main.html`, `edit_product.html`, and `create_product.html` inside the `main` directory on the `templates` subdirectory using the include `tags` at the top like:

    ```bash
    {% extends 'base.html' %}
    {% block content %}
    {% include 'navbar.html' %}
    ...
    {% endblock content%}
    ```

#### Customizing Create Product Page

Open the `create_product.html` file and change the code as follows:

    ```bash
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Create Product</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %} # That we have added earlier

    <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Product</h1>

        <div class="bg-gradient-to-r from-orange-400 to-teal-400 shadow-md rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
            <div class="flex flex-col">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                {{ field.label }}
                </label>
                <div class="w-full">
                {{ field }}
                </div>
                {% if field.help_text %}
                <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                {% endif %}
                {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
            </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
            <button type="submit" class="bg-orange-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                Create Product
            </button>
            </div>
        </form>
        </div>
    </div>
    </div>

    {% endblock %}
    ```

#### Cuztomizing Edit Product Page

Open the `edit_product.html` file and change the code as follows:

    ```bash
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Edit Product</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Mood Entry</h1>
    
        <div class="bg-gradient-to-r from-orange-400 to-teal-400 shadow-md rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
                <div class="flex flex-col">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                    </label>
                    <div class="w-full">
                        {{ field }}
                    </div>
                    {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
                <button type="submit" class="bg-orange-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                    Edit Mood Entry
                </button>
            </div>
        </form>
    </div>
    </div>
    </div>
    {% endblock %}
    ```

#### Cuztomizing Product List Page

Because we want to make it so that our products are listed as attractive and responsive, with an additional info that if there are no products, the product list would display an image and a message that no products are registers, we can implement it as follows

1. Firsly, we create a new file called `card_info.html` inside the `main` directory on the `templates` subdirectory, then fill it in with the following HTML code:

    ```bash
    <div class="bg-orange-600 rounded-xl overflow-hidden border-2 border-teal-800">
        <div class="p-4 animate-shine">
        <h5 class="text-lg font-semibold text-white">{{ title }}</h5>
        <p class="text-teal-100">{{ value }}</p>
        </div>
    </div>
    ```

2. Next, we would make a new file called `card_product.html` in the same directory as before, and add the following code to display our products as a card like table:

    ```bash
    <div class="relative break-inside-avoid transition-transform transform hover:scale-105 duration-300 shadow-lg">
        <div class="relative bg-white border-2 border-teal-300 rounded-lg overflow-hidden h-full">
        <!-- Placeholder for product image -->
        <div class="bg-teal-100 h-40 flex items-center justify-center">
            <span class="text-teal-700 font-bold text-2xl">{{ product_entry.category|title }}</span>
        </div>
    
        <!-- Product Details -->
        <div class="p-4">
            <h3 class="font-bold text-2xl text-teal-600 mb-1">{{ product_entry.name }}</h3>
            <p class="text-gray-700 text-lg mb-2">Rp{{ product_entry.price }},00 </p>
            <p class="text-sm text-gray-600">{{ product_entry.description|truncatewords:15 }}</p>
    
            <!-- Rating and Stock -->
            <div class="mt-4 flex items-center justify-between">
            <div class="flex items-center space-x-1">
                {% if product_entry.is_high_rating %}
                <span class="text-yellow-500 font-bold">★</span>
                <span class="text-gray-800 text-sm">{{ product_entry.rating }}</span>
                {% else %}
                <span class="text-gray-500 text-sm">Rating: {{ product_entry.rating }}</span>
                {% endif %}
            </div>
            <div class="text-sm {{ product_entry.stock|yesno:'text-green-500,text-red-500' }}">
                Stock: {{ product_entry.stock }}
            </div>
            </div>
        </div>
    
        <!-- Buttons (Edit/Delete) -->
        <div class="absolute top-2 right-2 flex space-x-1">
            <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-orange-500 hover:bg-orange-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
            </a>
            <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
            </a>
        </div>
        </div>
    </div>
    ```

    Now in this case, we have customized our `main` page such that we would display the products as a card and added edit and delete buttons on the top right of the cards.

3. Now to add an image if there are no products available. Here I used a famous video game character, called *Pathfinder* from the game *Apex Legends* displaying a sad face. I renamed the `png` file as `sad-pathfinder.png`. Now we have to modify `main.html` so that it can use the `card_info.html`, `card_product.html` and the sad `png` file. Remember that `main.html` is in the same directory that we are currently modifying that is `main/templates`. Change the `main.html` file as follows:

    ```bash
    {% extends 'base.html' %}
    {% load static %}

    {% block meta %}
    <title>Pixel Play</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
    <div class="p-2 mb-6 relative">
        <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
        {% include "card_info.html" with title='NPM' value=npm %}
        {% include "card_info.html" with title='Name' value=name %}
        {% include "card_info.html" with title='Class' value=class %}
        </div>
        <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
        <div class="w-full min-h-4 bg-teal-600"></div>
        </div>
        <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
        <div class="h-full min-w-4 bg-teal-600 mx-auto"></div>
        </div>
    </div>

    <div class="px-3 mb-4">
        <div class="flex rounded-md items-center bg-teal-600 py-2 px-4 w-fit">
        <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
        </div>
    </div>

    <div class="flex justify-end mb-6">
        <a href="{% url 'main:create_product' %}" class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
            Add New Product
        </a>
    </div>

    {% if not products %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sad-pathfinder.png' %}" alt="Sad face" class="w-120 h-50 mb-4"/>
        <p class="text-center text-gray-600 mt-4">There are no products available.</p>
    </div>
    {% else %}
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">
        {% for product in products %}
            {% include 'card_product.html' with product_entry=product %}
        {% endfor %}
    </div>
    {% endif %}
    </div>
    {% endblock content %}
    ```

4. To add the `sad-pathfinder.png` file, we have to make a new subdirectory inside the `static` directory on the `root` of our project called `image`. So, our `png` file would be inside of `static/image` directory.

Now we are officially done and we have just made our website more attractive!

### Answers to the Questions

1. **If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!**

    The priority order, just like we can see on Slide 06 about *Web Design Using HTML5 and CSS3.pdf*, determines which styles will apply when multiple CSS selectors target the same HTML element. The order of priority from highest to lowest are:

    1. Inline Styles
    2. ID Selectors
    3. Class Selectors, Attribute Selectors, Pseudo-classes
    4. Element Selectors

2. **Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!**

    Because it ensures that a website or web application can provide and improve user experience across any devices, in our case accross desktop computers to tablets and smartphones. Responsive design also allows content to be flexible without the need for updates and versions of the same website.

    Examples of Application with Responsive Design:
    
    1. Tokopedia <br>
            Tokopedia adjusts its layout to fit various screen sizes. Even on mobile devices, the screen resolution of let's say and Iphone and Android are different, but Tokopedia manages to provide user with optimized sidebars and navigation options.

    2. Twitter (X) <br>
            Twitter (X) being a Social Media can change its layout based on mobile or dekstop, there are some unofficial sources online that say Twitter (X) can be run on Smartfridges.
    
    Examples of Application **without** Responsive Design:

    1. Some University's Faculty Websites <br>
            Older universities websites might not have responsive layouts. These systems are designed for desktop users, without constant updates, making them difficult to navigate on smaller screens.

3. ** Explain the differences between margin, border, and padding, and how to implement these three things!**

    1. Margin : <br>
        The margin is the outermost space that separates an element from its neighboring elements. It defines the space outside the border of an element. Margins are used to create space between different elements on the page, preventing them from touching or overlapping.

    Implementation : 
        
        ```bash
                /* Apply the same margin to all sides */
        .element {
            margin: 20px;
        }

        /* Different margins for each side */
        .element {
            margin-top: 10px;
            margin-right: 15px;
            margin-bottom: 20px;
            margin-left: 25px;
        }

        /* Center an element horizontally */
        .centered {
            margin-left: auto;
            margin-right: auto;
        }
        ```


    2. Border : <br>
    
        The border is the line that wraps around the element’s content and padding. It lies between the margin and the padding. Borders are used to visually separate or highlight an element. Borders can have different styles (solid, dashed, dotted, etc.) and can be of varying widths and colors.

    Implementation : 
        ```bash
                /* Simple border for all sides */
        .element {
            border: 2px solid black;
        }

        /* Different borders for each side */
        .element {
            border-top: 5px dashed red;
            border-right: 2px solid blue;
            border-bottom: 3px dotted green;
            border-left: 1px solid black;
        }
        ```

    3. Padding : <br>
    
        The padding is the space between the content of an element and its border. It creates space inside the element, pushing the content away from the edges. Padding is used to create space inside an element to make the content look more visually appealing, preventing the text or images from sticking too closely to the border.

    Implementation :
        ```bash
                /* Same padding for all sides */
        .element {
            padding: 15px;
        }

        /* Different padding for each side */
        .element {
            padding-top: 10px;
            padding-right: 20px;
            padding-bottom: 15px;
            padding-left: 25px;
        }
        ```

    **Differences**

    Margin : 
-       Controls the space outside the border.
-       Affects the distance between elements.
-       Does not affect the size of the element itself.

    Border :
-       A visual line that wraps around the padding and content.
-       Can have styles, width, and color.
-       Affects the overall size of the element (thicker borders will increase the element's size).
    
    Padding :
-       Controls the space inside the border.
-       Affects the space between the content and the border, making the content look less crowded.
-       Increases the size of the element without changing the outer margin.

4. **Explain the concepts of flex box and grid layout along with their uses!**

    1. Flexbox (Flexible Box Layout)
        
        Concept:
        
        Flexbox is a one-dimensional layout model designed for aligning and distributing space among items in a single direction (either horizontally or vertically). Flexbox is best suited for arranging elements along a row or a column.
    
    2. CSS Grid Layout
        
        Concept:
        
        Grid is a two-dimensional layout system, meaning it can handle layouts in both rows and columns simultaneously. CSS Grid is more suitable for more complex, grid-based designs, where control over both axes (horizontal and vertical) is required.

5. **How do I implement the checklist above step-by-step**

    Already answered on top of this section 🙏😁