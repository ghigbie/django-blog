from django.shortcuts import render
from .data_set import *

def index(request):
    return render(request, "blog/index.html", {
        "posts": posts
    })


def about(request):
    return render(request, "blog/about.html")

