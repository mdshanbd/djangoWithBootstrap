
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about', views.aboutpage, name='aboutpage'),
    path('contact', views.contactpage, name='contactpage'),
    path('portfolio', views.portfoliopage, name='portfoliopage'),
]
