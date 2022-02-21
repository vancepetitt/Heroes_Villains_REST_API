from django.urls import path
from . import views

#changing the path to '' allows for the path to use what is pulled from views.py
urlpatterns = [
    path('', views.supers_list),
]