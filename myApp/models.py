from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER = [
      
        ('customer','Customer'),
        ('garageowner','Garageowner'),
        ('admin','Admin')
    ]

    Profile_Photo= models.ImageField(upload_to= "media/Profile_Photo" , null= True)
    display_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    voter_id_no=models.CharField(max_length=100,)
    user_type = models.CharField(choices=USER , max_length=100)

    def __str__(self) -> str:
        return self.display_name

class Workshop_Registration(models.Model):

    Workshop_Name=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    area=models.CharField(max_length=100, null=True)
    trade_license=models.FileField(upload_to= "media/trade_license" , null= True)
    certifications=models.FileField(upload_to= "media/certifications" , null= True)
    Owner_Voter_ID=models.OneToOneField(Custom_User, on_delete=models.CASCADE, null =True , blank =True)
    Contact_Number=models.CharField(max_length=100, null=True)
    Password=models.CharField(max_length=100, null=True)
    confirm_Password=models.CharField(max_length=100, null=True)
    Number_of_employee=models.CharField(max_length=100, null=True)
    owner_photo= models.ImageField(upload_to= "media/owner_photo" , null= True)
    Workshop_Photo= models.ImageField(upload_to= "media/Workshop_Photo" , null= True)
    TIN=models.CharField(max_length=100, null=True)
    Service_Type=models.TextField(max_length=100, null=True)
    Vehicle_Brand=models.CharField(max_length=100, null=True)
    Rating=models.IntegerField(null=True)
    
    
    
    def __str__(self) -> str:
        return self.Workshop_Name

class Receive_Service(models.Model):
    Workshop_Name=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Service_Type=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    customer_name=models.ForeignKey(Custom_User, on_delete=models.CASCADE, null =True , blank =True)
    Vehicle_Brand=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Vehicle_Registration_Number=models.CharField(max_length=100, null=True)
    Completion_Date=models.DateTimeField(auto_now_add=True, null =True)

class Service_Completion(models.Model):
    Workshop_Name=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Service_Type=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Vehicle_Brand=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Delivery_Date=models.DateTimeField(auto_now_add=True, null =True)
    Bill_amount=models.CharField(max_length=100, null=True)
    Invoice=models.FileField(upload_to= "media/Invoice" , null= True)
    Vehicle_Registration_No=models.ForeignKey(Receive_Service, on_delete=models.CASCADE, null =True , blank =True)
    Rating=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)

class Cancelled_Service(models.Model):
    customer_name=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Workshop_Name=models.ForeignKey(Workshop_Registration, on_delete=models.CASCADE, null =True , blank =True)
    Cancel_reason=models.TextField(max_length=100, null=True)
    Area=models.TextField(max_length=100, null=True)
    








