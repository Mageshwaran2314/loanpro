from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate, login


class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if not user:
    #             raise forms.ValidationError("Username does not exists")
    #         if user.checkpassword(password):
    #             raise forms.ValidationError("Wrong Password")
    #         return render(request, 'invalid.html')
