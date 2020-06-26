from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.POST.get('next', '/accounts/profile/'))
                else:
                    return HttpResponse("Konto jest zablokowane")
        else:
            return HttpResponse("Nieprawidłowe dane")

    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('przepisowo_site:recipes-list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return render(request, 'accounts/welcome.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm
    return render(request, 'accounts/register.html', {'user_form': form})
