from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic, Appointment


# Create your views here.

def index(request : HttpRequest):
    
    clinics = Clinic.objects.all()
    return render(request, "main/index.html",{"clinics": clinics})

def clinic_detail(request : HttpRequest):
    return render(request, "main/clinic_detail.html")

def about(request : HttpRequest):
    return render(request, "main/about.html")


# def manage_clinics(request : HttpRequest):
#     return render(request, "main/manage_clinics.html")

def add_clinic(request : HttpRequest):

    if not request.user.is_staff:
        return redirect("main:index_page")

    if request.method == "POST":
        #to add a new entry
        new_clinic = Clinic(name= request.POST["name"], description = request.POST["description"], department = request.POST["department"], established_at=request.POST["addition_date"], feature_image = request.FILES["feature_image"])
        new_clinic.save()
        # return redirect("games:latest_games_page")
    clinics = Clinic.objects.all()

                                                         #  {"form": department}
    return render(request, "main/manage_clinics.html",{"clinics": clinics},)


def update_clinic(request : HttpRequest, clinic_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.established_at = clinic.established_at.isoformat() #to make it compatible with input value in html
    if request.method == "POST":
        clinic.name = request.POST["name"]
        clinic.description = request.POST["description"]
        clinic.department = request.POST["department"]
        clinic.established_at = request.POST["established_at"]
        #to check if user chosen a file to upload for the update
        if "feature_image" in request.FILES:
            clinic.feature_image = request.FILES["feature_image"]

        clinic.save()
        return redirect("main:add_clinics_page")

    return render(request, "main/update_clinic.html", {"clinic" : clinic})


def delete_clinic(request : HttpRequest, clinic_id):
    if not request.user.is_staff:
        return redirect("main:index_page")

    clinic = Clinic.objects.get(id=clinic_id)
    clinic.delete()
    return redirect("main:add_clinics_page")

def clinic_detail(request : HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)
    # reviews = Review.objects.filter(game=game)
                                                     # , "reviews" : reviews
    return render(request, "main/clinic_detail.html", {"clinic" : clinic})


def search(request : HttpRequest): 

    # display = int(request.GET.get("display", 10)) how many in every page

    if 'search' in request.GET:
        clinics = Clinic.objects.filter(name__contains=request.GET["search"])
    else:
        clinics = Clinic.objects.all()

    context = {"clinics" : clinics}
    return render(request, "main/search.html", context)



def manage_appointments(request : HttpRequest):
    if not request.user.is_staff:
        return redirect("main:index_page")
    return render(request, "main/manage_appointments.html")


def book_appointment(request : HttpRequest):
    if not request.user.is_authenticated:
        return redirect("accounts:login_user")
    return render(request, "main/manage_appointments.html")




