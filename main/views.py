from django.shortcuts import render

def home(request):
    data = {
        'title': 'Home',
    }
    return render(request, 'main/home.html' , data )

def about(request):
    data = {
        'title': 'About',
    }
    return render(request, 'main/about.html' , data )

