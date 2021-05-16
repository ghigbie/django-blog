from django.http.response import Http404
from django.shortcuts import render
from .data_set import *

def index(request):
    return render(request, "blog/index.html", {
        "posts": "moo"
    })

def about(request):
    return render(request, "blog/about.html")

def posts(request):
    return render(request, "blog/posts_page.html")

def post(request, slug):
    return render(request, "blog/post_detail.html")
    # except:
    #     raise Http404("not found : (")