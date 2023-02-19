from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_login(request:HttpRequest):
    loggin_msg = ''
    
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

        if user is not None:
            #login user
            login(request, user)
            return redirect("main:home_page")
        else:
            loggin_msg = "Please Use correct Credentials"

    return render(request, "accounts/login.html", {"msg" : loggin_msg})

def user_logout(request:HttpRequest):
    logout(request)

    return redirect("main:home_page")

def user_register(request:HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()

        return redirect(request,"accounts/login.html")


    return render(request, "accounts/register.html")


