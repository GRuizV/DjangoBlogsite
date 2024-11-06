from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Post



def home(request: HttpRequest) -> HttpResponse:

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context=context)



def about(request: HttpRequest) -> HttpResponse:

    return render(request, 'blog/about.html', context = {'title': 'About'})


# Blog Detail View

def Blog_Detail(request,pk):
    blog = Post.objects.get(id = pk)
    context = {
        "blog" : blog
    }

    return render(request,"enter file name.html",context)







