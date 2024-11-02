from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # This saves the User if the form is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')   # Flash message
            return redirect('login')
                
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', context = {'form': form} )



@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/profile.html')






















