from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306172325',
        'name': 'Andriyo Averill Fahrezi',
        'class': 'KKI'
    }

    return render(request, "main.html", context)