from django.urls import path
from .api import *

urlpatterns = [
    path('list/<int:page>/', post_list, name='get_posts'),
    path('rate_post/', rate_post, name='rate_post'),
    path('rate_post/<int:post_id>/rated/users/<int:page>/', rate_list, name='lsit-rated-users-'),
]