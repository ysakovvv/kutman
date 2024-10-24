from django.urls import path
from .views import *


urlpatterns=[
    path('',about),
    path('index', index),
    path('contact/',contact),
    path('kutman/',kutman),
]