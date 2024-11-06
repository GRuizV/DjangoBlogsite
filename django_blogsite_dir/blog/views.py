from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Post
from comments.models import Comments



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

    if request.POST:
        user = request.user
        post = blog
        message = request.POST.get("message")

        comment = Comments.objects.create(
            user = user,
            post = post,
            message = message
        )
        
        comment.save()

    return render(request,"enter file name.html",context)







