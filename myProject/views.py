from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def homePage(request):
    return render(request,'home.html')

def signupPage(request):
    if request.method == "POST":
        display_name = request.POST.get('display_name')
        Profile_Photo = request.POST.get('Profile_Photo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        voter_id_no = request.POST.get('voter_id_no')
        user_type = request.POST.get('user_type')

        user = Custom_User.objects.create_user(username = display_name, password = password )

        user.display_name =display_name 
        user.email = email
        user.user_type = user_type
        user.Profile_Photo = Profile_Photo
        user.confirm_password = confirm_password
        user.address = address
        user.voter_id_no = voter_id_no
        user.user_type = user_type
    
    
        user.save()
        
        return redirect("signinpage")

       
    return render(request,"signup.html")


def signinpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user:
            login(request, user)
            return redirect ("homePage")


    return render(request,"signinpage.html")

def CusomerSingup(request):
    return render(request,"customer/customerSingup.html")
    

def logoutPage(request):
    logout(request)
    return redirect("signinpage")

# def garage_regestration(request):
#     if request.method == "POST":
#         workshopName = request.POST.get("workshopName")
#         address = request.POST.get("address")
#         area = request.POST.get("area")
#         tradeLicense = request.POST.get("tradeLicense")
#         certifications = request.POST.get("certifications")
#         ownerVoterId = request.POST.get("ownerVoterId")
#         contactNumber = request.POST.get("contactNumber")
#         ownerphoto=request.POST.get("ownerphoto")
#         workshopPhoto = request.POST.get("workshopPhoto")
#         numOfEmployees = request.POST.get("numOfEmployees")
#         tin = request.POST.get("tin")
#         serviceType = request.POST.get("serviceType")
#         vehicleBrand = request.POST.get("vehicleBrand")
        
#         register=Workshop_Registration(
#             Workshop_Name=workshopName,
#             Address=address,
#             area=area,
#             trade_license=tradeLicense,
#             certifications=certifications,
#             Owner_Voter_ID=ownerVoterId,
#             Contact_Number=contactNumber,
#             owner_photo=ownerphoto,
#             Workshop_Photo=workshopPhoto,
#             TIN=tin,
#             Service_Type=serviceType,
#             Vehicle_Brand=vehicleBrand,
#             Number_of_employee=numOfEmployees,
           
#         )
      
        
#     return render(request,"garageowner/registration.html" )

