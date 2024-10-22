from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



def home(request: HttpRequest) -> HttpResponse:

    return HttpResponse('<h1>Blog Home</h1>')



def about(request: HttpRequest) -> HttpResponse:

    return HttpResponse('<h1>Blog About</h1>')












