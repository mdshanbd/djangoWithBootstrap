from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'home.html')


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    return render(request, 'contact.html')


def portfoliopage(request):
    return render(request, 'portfolio.html')
