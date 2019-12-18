from django.shortcuts import render
from accounts.forms import login_form
from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        print(request.POST.dict())
        form = login_form(request.POST or None)
        if form.is_valid():
           print("VALID")
           username = form.cleaned_data.get("username")
           print(1)
           password = form.cleaned_data.get("password")
           print(2)
           print(username, password)
           print(3)
           user = authenticate(username=username, password=password)
           print(4)
           # login(request,user)
           if user:
               # redirect to a new URL:
               return HttpResponseRedirect('/submit_course/')
           print(5)
    return render(request, 'login.html', {'form': form})
