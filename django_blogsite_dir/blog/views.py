from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



# Dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Aug 27, 2018'
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Aug 28, 2018'
    }
]


def home(request: HttpRequest) -> HttpResponse:

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context=context)



def about(request: HttpRequest) -> HttpResponse:

    return render(request, 'blog/about.html', context= {'title': 'About'})












