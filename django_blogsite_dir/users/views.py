from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # This saves the User if the form is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')   # Flash message
            return redirect('blog-home')
                
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', context = {'form': form} )






















