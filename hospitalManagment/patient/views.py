from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest,HttpResponse

# Create your views here.


def Register_patiend(request : HttpRequest):
    
    if request.method == 'POST':
        new_user = User.objects.create_user(username = request.POST['username'],email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
        new_user.save()
        return redirect('patient:signin')
    return render(request , 'patient/Sign_up.html')    



def sign_in(request :HttpRequest):

    if request.method =='POST':
        user = authenticate(request , username = request.POST['username'] , password = request.POST["password"])


        if user is not None:
            login(request , user)
            return redirect('main:home')
        else:
            return render(request , 'Patient/Sign_in.html' )
    return render(request , 'patient/sign_in.html')   



def log_out_user(request : HttpRequest):
    logout(request)
    return redirect ( 'main:home')