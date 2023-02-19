from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinc, Review, Doctor, Appointment, User
from django.contrib import messages
from datetime import datetime

# main pages

def index_page(request : HttpRequest):
   
    return render(request , "main/index.html")

def about_page(request : HttpRequest):
   
    return render(request , "main/about.html")

def departments_page(request : HttpRequest):
    

    context = {"departments_page" : departments_page}
    return render(request, "main/departments.html", context)
   
def doctors_page(request : HttpRequest):
    
   
    return render(request , "main/doctors.html")


def contact_page(request : HttpRequest):
   
    return render(request , "main/contact.html")




# add,delet,search,views and etc ....


def add_clinc(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:login_user")

    if request.method == "POST":
        #to add a new entry
        new_clinc = Clinc(name = request.POST['name'] ,description = request.POST['description'] ,departments = request.POST['departments'], established_at = request.POST['established_at'] , image = request.FILES["image"])
        new_clinc.save()
        return redirect("main:departments_page")


    return render(request, "main/add.html")


def add_doctor(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("accounts:login_user")

    if request.method == "POST":
        #to add a new entry
        new_doctor = Doctor(name= request.POST["name"], description = request.POST["description"], image = request.FILES["image"])
        new_doctor.save()
        return redirect("main:doctors_page")


    return render(request, "main/add_doctor.html")



def update_clinc(request :HttpRequest , clinc_id):
        
    clinc = Clinc.objects.get(id = clinc_id)
    if request.method == 'POST':
            clinc.name = request.POST['name'],
            clinc.description=request.POST['description'],
            clinc.departments=request.POST['departments'],
            if "image" in request.FILES:
                clinc.image = request.FILES["image"]
            if "established_at" in request.POST:
                clinc.established_at=request.POST['established_at']   
                clinc.save()
            return redirect('main:departments_page')
        
    return render(request , 'main/update_clinc.html',{'clinc':clinc})    
    

 




def delete_clinc(request : HttpRequest, clinc_id):

    if not request.user.has_perm("main.delete_clinc"):
       return render(request, "main/no_permission.html")
    

    clinc = Clinc.objects.get(id=clinc_id)
    clinc.delete()
    return redirect("main:departments_page")



def add_review(request : HttpRequest, clinc_id):

    if request.method == "POST":
        clinc = Clinc.objects.get(id=clinc_id)
        new_review = Review(user = request.user, clinc=clinc, content = request.POST["content"])
        new_review.save()

    return redirect("main:clinc_detail", clinc_id=clinc_id)



def clinc_detail(request : HttpRequest, clinc_id):

    clinc = Clinc.objects.get(id=clinc_id)
    reviews = Review.objects.filter(clinc=clinc)




    return render(request, "main/clinc_detail.html", {"clinc" : clinc, "reviews" : reviews})



def show_all_clinc(request:HttpRequest):
        
        all_clinc = Clinc.objects.all()
        
        return render(request , 'main/departments.html' , { 'all_clinc': all_clinc })
    

def show_all_doctor(request:HttpRequest):
        
        all_doctor = Doctor.objects.all()
        
        return render(request , 'main/doctors.html' , {'all_doctor': all_doctor})




def search_clinc(request : HttpRequest):
    if request.method == "POST":
        search = request.POST['search']
        search_clinc = Clinc.objects.filter(name__contains=search)

        return render(request, "main/search.html", {'search_clinc':search_clinc}) 
    else:
        return render(request, "main/search.html", {})
    


# Appo


