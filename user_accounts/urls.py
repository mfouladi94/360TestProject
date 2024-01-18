from django.contrib import admin
from django.urls import path, include
from .api import *

urlpatterns = [
    path('signup/', signup),
    path('profile/', ProfileApi.as_view()),

]