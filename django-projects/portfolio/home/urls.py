
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),   
    path('about', views.about, name='about'), # just add the name not the / in the front.   
]
