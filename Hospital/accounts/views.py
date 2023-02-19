from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_login(request:HttpRequest):
    pass

def user_logout(request:HttpRequest):
    pass

def user_register(request:HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()

        return redirect("accounts:login_user")


    return render(request, "accounts/register.html")


