from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from travelbook.models import Contact
from travelbook.models import Flights
from travelbook.models import Booking
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
   return render(request,"index.html")

def signin(request):
   return render(request,"login.html")
@login_required(login_url="")
def mybooking(request):
   return render(request,"mybooking.html")

@login_required(login_url="")  
def bookingreceipt(request):
   return render(request,"bookingreceipt.html")
   
   
def about(request):
   return render(request,"about.html")

@login_required(login_url="")
def payment(request):
   return render(request,"payment.html")

def handleSignup(request):
   if request.method=='POST':
      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']

      myuser=User.objects.create_user(username,email,password)
      myuser.save()
      return redirect('signin')
   else:
      return HttpResponse(" NOT FOUND")
   return render(request,"login.html")
   
def handleLogin(request):

   if request.method =='POST':

      loginusername=request.POST.get('loginusername')
      loginpassword=request.POST.get('loginpassword')

      user=authenticate(request,username=loginusername,password=loginpassword)
      
      if user is not None:

         login(request,user)
         #messages.success(request,"Successfully Logged In")
         return redirect('user')
      else:
         return HttpResponse("user or password is incorrect")
      
   return render(request,'user.html',info)
   
@login_required(login_url="")
def user(request):
   
   return render(request,"user.html")
def contact1(request):


   if request.method=='POST':
      #always keep different names of key in different forms eg,contact-username in contact form and username in signup
      username=request.POST.get('contact-username')
      email=request.POST.get('contact-email')
      phone=request.POST.get('contact-phone')
      message=request.POST.get('contact-message')
      contact=Contact(username=username,email=email,phone=phone,message=message)
      contact.save()
      return redirect('home')
   else:
      return HttpResponse("something went wrong")
   return render(request,"index.html")

@login_required(login_url="")
def bkr(request):
   z=[]
   
   flightdata=Flights.objects.all()
   
      
   
   
   bookdata=Booking.objects.all()
   for i in bookdata:
      z.append(i)
   print(z)  
   data={
      'flightdata':flightdata,
      'bookdata':bookdata,
      'z':z,
      
   }
   
   return render(request,'booking.html',data)

@login_required(login_url="")
def thanks(request):
   return render(request,'thanks.html')

@login_required(login_url="")
def bookingreceipt(request):
   
   flightdata=Flights.objects.all()
   
      
   
   bookdata=Booking.objects.all()
      
   data={
      'flightdata':flightdata,
      'bookdata':bookdata,
      
      
      
   }
   return render(request,'bookingreceipt.html',data)

def logOUT(request):
   logout(request)
   return redirect('signin')
