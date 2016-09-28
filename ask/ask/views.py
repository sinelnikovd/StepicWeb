from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ask.forms import SignupForm, LoginForm


def signup(request, *args, **kwargs):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def loginSite(request, *args, **kwargs):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})