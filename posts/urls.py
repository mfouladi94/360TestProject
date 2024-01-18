from django.urls import path
from .api import *

urlpatterns = [
    path('list/<int:page>/', post_list, name='get_posts'),
    path('rate_post/', rate_post, name='rate_post'),
    path('rate_post/<int:pk>/rated/users/', rate_post, name='-rated-users-'),
]