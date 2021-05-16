from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('posts/', posts, name="posts_page"),
    path("posts/<slug:slug>", post, name="post_detail")
]
