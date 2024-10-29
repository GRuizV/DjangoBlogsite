from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', context = {'form': form} )




















