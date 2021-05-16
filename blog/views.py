from django.http.response import Http404
from django.shortcuts import render
from .data_set import *

def get_data(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts, key=get_data)
    latest_posts = sorted_posts[-3:]
    print(latest_posts)
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def about(request):
    return render(request, "blog/about.html")

def posts(request):
    return render(request, "blog/posts_page.html", {
        "posts": all_posts
    })

def post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    try:
        return render(request, "blog/post_detail.html", {
            "post": post
        })
    except:
        raise Http404("not found : (")