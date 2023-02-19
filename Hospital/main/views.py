from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import User,Clinic,Appointment
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import datetime


# from django.shortcuts import render ,redirect
# from django.http import HttpRequest, HttpResponse
# from .models import Clinic, Appointment
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout




# # Create your views here.

# def Home_page(request : HttpRequest):
#     result = Clinic.objects.all()
    
#     context = {
        
#         "clinics":result
#     }
    
#     return render(request, "main/Home.html",context)


# def details_page(request : HttpRequest , clinic_id):
#     result = Clinic.objects.get( id = clinic_id)
#     context = {
        
#         "clinic" : result
#     }
#     return render(request, "main/details.html",context)



# def add_new_page(request : HttpRequest):
#     if request.method == "POST":
#            Clinic(
#             name = request.POST["name"] ,
#             description = request.POST["description"], 
#             image =request.FILES["image"]
#             ).save()
    
#     return render(request, "main/add_new.html")


# def booking(request : HttpRequest , clinic_id):
#     msg = "Appointment date booked"
#     if request.method == "POST":
            
#         clinic = Clinic.objects.get(id = clinic_id)
#         check_date= Appointment.objects.filter(date__gt= request.POST["date"])
#         if check_date:
#             return render(request ,"main/booking.html" ,{"msg" :msg})
#         else:
#             Appointment(
#             clinic= clinic,
#             user = request.user,
#             date = request.POST["date"],
#             patient_age = request.POST["age"],
#             description = request.POST["description"]).save()
            
#         return redirect("url_main:appointment_page" , clinic_id = clinic_id )
#     return render(request, "main/booking.html")



# def search(request : HttpRequest):

#     if request.method == "GET": 

#             name =  request.GET.get('search')      
#             search = Clinic.objects.filter(name__contains = name)
               
#             return render(request , "main/search.html" , {"search" : search})



# def delete(request : HttpRequest, clinic_id):
#     post = Clinic.objects.get(id=clinic_id)
#     post.delete()
#     return redirect("main/Home.html")



# def update(request : HttpRequest , clinic_id ):

#     clinic = Clinic.objects.get(id = clinic_id)

#     if request.method == "POST":
#             clinic.name = request.POST["name"]
#             clinic.description = request.POST["description"]
#             clinic.image = request.FILES["image"]
#             clinic.save()
#             return redirect("main/Home.html")
#     return render(request , "main/update.html" ,  {"clinic" : clinic})



# def mange(request : HttpRequest):
    
#     result = Clinic.objects.all()
#     context = {
        
#         "clinics":result
#     }
    
#     return render(request , "main/mange.html" , context)



# def appointments (request : HttpRequest ):
    
#     result = Appointment.objects.all()
    
#     context = {
        
#         "appointments":result
#     }
    
#     return render(request , "main/appointments.html" , context)
    



# def login_page(request : HttpRequest):
#      loggin_msg = None
    
#      if request.method == "POST":
#         #authenticate user credentials
#         user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

#         if user is not None:
#             #login user
#             login(request, user)
#             return redirect("url_main:h_page")
#         else:
#             loggin_msg = "Please Use correct Credentials"

#      return render(request, "main/login.html", {"msg" : loggin_msg})
#      return render(request, "main/login.html")

# def logout_user(request : HttpRequest):

#     logout(request)

#     return redirect("main/Home.html")

# def clinics_page(request : HttpRequest):
#     return render(request, "main/clinics.html")



# def register_page(request : HttpRequest):
#     if request.method == "POST":
#         new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
#         new_user.save()
#     return redirect("main:login_page")
    
#     return render(request, "main/register.html")
        
    
from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import User,Clinic,Appointment
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import datetime


# Create your views here.

def home_page(request :HttpRequest):
    Clinics = Clinic.objects.all()
    
    return render(request , 'main/Home.html' ,{'Clinics':Clinics} )
    

    

def addClinec (request : HttpRequest):
    if request.user.is_staff:
        if request.method == 'POST':
            new_clinec = Clinic(name = request.POST['name'] , feature_image = request.FILES['feature_image'],description = request.POST['description'] , departments = request.POST['departments'] ,established_at = request.POST['established_at'])
            new_clinec.save()
            return redirect('main:home')
        return render(request , 'main/add_new.html')
    return redirect('patient:signin')  


def upadateclinec(request :HttpRequest , clinec_id):
    if request.user.is_staff:
        updated_clinec=Clinic.objects.get(id = clinec_id)
        updated_clinec.established_at=updated_clinec.established_at.isoformat() 
        if request.method == 'POST':
            updated_clinec.name = request.POST['name'],
            updated_clinec.description=request.POST['description'],
            updated_clinec.departments=request.POST['departments'],
            if "feature_image" in request.FILES:
                updated_clinec.feature_image = request.FILES["feature_image"]
            if "established_at" in request.POST:
                updated_clinec.established_at=request.POST['established_at']   
            updated_clinec.save()
            return redirect('main:allcl')
        return render(request , 'main/update.html',{'updated_clinec':updated_clinec})    
    return redirect('patient:signin')


def deletclinec(request :HttpRequest , clinec_id):
    if request.user.is_staff:
        deleted_clinec = Clinic.objects.get(id=clinec_id)
        deleted_clinec.delete()
        return redirect('main:home')


def show_all_clinec(request:HttpRequest):
    if request.user.is_authenticated:
        if 'search' in request.GET:
            all_clinec = Clinic.objects.filter(name__contains=request.GET["search"])
        else:
            all_clinec = Clinic.objects.all()
        
        return render(request , 'main/mange.html' , {'all_clinec':all_clinec})
    return redirect('patient:signin')

def check_availbal_date(date1 : datetime , date2 :datetime) -> bool:
    if date1 == date2:
        return True
    else:
        return False



def bookForClinec(request :HttpRequest , clinec_id):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
             
            clinec_selected = Clinic.objects.get(id=clinec_id)
            new_appointments = Appointment(appointmentUser = request.user , apclinec = clinec_selected ,case_description=request.POST['case_description'], patient_age = request.POST['patient_age'],appointment_datetime = request.POST['appointment_datetime'] )
            check_dateTime = Appointment.objects.filter(appointment_datetime = request.POST['appointment_datetime'])
            
            if check_dateTime :
                messages.success(request , 'soory chose another date and time')

            else:      
                new_appointments.save()
                return redirect('main:home')
        return render(request,'main/booking.html')
    
    

def showUserbook(request : HttpRequest ):
    if request.user.is_authenticated:
        name_of_patient = request.user.get_username    
        show_booked = Appointment.objects.filter(appointmentUser = request.user.id)
        return render(request , 'main/booking_details.html', {'show_booked':show_booked , 'name_of_patient':name_of_patient})
    return redirect('patient:signin')
        
    

def veiw_appointmentin_clinec(request : HttpRequest , clinec_id):
    if request.user.is_staff:
        name_of_clinec = Clinic.objects.get(id = clinec_id)
        all_appointment_for_one_clinec = Appointment.objects.filter(apclinec = clinec_id)
        return render (request , 'main/appointment_clinics.html',{'all_appointment_for_one_clinec':all_appointment_for_one_clinec , 'name_of_clinec':name_of_clinec})
    return redirect('main:home')

def control_one_appontment_for_clinec(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        
        slected_appintment = Appointment.objects.get(id = appointment_id)
        
        return render(request,'main/appintment_patient.html',{'slected_appintment':slected_appintment })
    return redirect('main:home')    

def delete_userappointment_by_admin(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        deleted_appointment = Appointment.objects.get(id = appointment_id)
        deleted_appointment.delete()
        return redirect('main:home')
    
def add_appointments_by_admin(request :HttpRequest ):
    user_assigend = User.objects.all()
    clinec_assiend = Clinic.objects.all()
    if request.method == 'POST':
        user = User.objects.get(id = request.POST['appointmentUser'])
        clinec = Clinic.objects.get(id = request.POST['apclinec'])
    
        new_appontment = Appointment(appointmentUser = user ,apclinec = clinec , case_description = request.POST['case_description'] ,patient_age = request.POST['patient_age'],appointment_datetime = request.POST['appointment_datetime'])

        new_appontment.save()
        return redirect('main:home')
    return render(request , 'main/add_new.html',{'user_assigend':user_assigend , 'clinec_assiend':clinec_assiend})

def update_appointment_by_admin(request :HttpRequest , appointment_id):
    if request.user.is_staff:
        updated_appointment = Appointment.objects.get(id = appointment_id)
        updated_appointment.appointment_datetime=updated_appointment.appointment_datetime.isoformat()
        if request.method == 'POST':
            updated_appointment.case_description=request.POST['case_description'],
            updated_appointment.patient_age = request.POST['patient_age']
            
            updated_appointment.appointment_datetime=request.POST['appointment_datetime']
               
            updated_appointment.is_attended=request.POST['is_attended']
            updated_appointment.save()
            return redirect('main:home') 
        return render(request , 'main/update.html' , {'updated_appointment':updated_appointment})   

 



