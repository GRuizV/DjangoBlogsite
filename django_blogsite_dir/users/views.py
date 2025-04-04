from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # This saves the User if the form is valid
            messages.success(request, f'Your account has been created! You are now able to log in!')   # Flash message
            return redirect('login')
                
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', context = {'form': form} )



@login_required
def profile(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid:

            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')   # Flash message
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context=context)






















