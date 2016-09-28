#coding: utf-8
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    username.widget.attrs['class'] = 'form-control'
    email = forms.EmailField()
    email.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['class'] = 'form-control'
    def save(self):
        return User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'],self.cleaned_data['password'])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    username.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['class'] = 'form-control'
    def clean(self):
        self.user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if self.user is None:
            raise forms.ValidationError(u'Не правильный логин или пароль')
    def save(self):
        return self.user