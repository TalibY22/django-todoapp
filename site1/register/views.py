from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def new_user(response):
    if response.method =="POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        return redirect("/create")
    else:
      form = UserCreationForm()
    return render(response, "register/Register.html",{"form":form})