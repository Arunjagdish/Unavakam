from django.http import HttpResponse
from django.template import loader
from .models import feedbacktable
from .models import bookingtable
from django .shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def Menu(request):
    template=loader.get_template('Menu.html')
    return HttpResponse(template.render())

def Soups_Menu(request):
    template=loader.get_template('Soups_Menu.html')
    return HttpResponse(template.render())

def Starters_Menu(request):
    template=loader.get_template('Starters_Menu.html')
    return HttpResponse(template.render())

def Catering(request):
    template=loader.get_template('Catering.html')
    return HttpResponse(template.render())

def Feedback(request):
    mydata=feedbacktable.objects.all()
    if(mydata!=""):
        return render(request,"Feedback.html",{"feedbacktable":mydata})
    else:
        return render(request,"Feedback.html")
    
def feedbackdata(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        age=request.POST["age"]
        role=request.POST["role"]
        userrecommend=request.POST["userrecommend"]
        mostLike=request.POST["mostLike"]
        prefer=request.POST["prefer"]
        comment=request.POST["comment"]

        obj=feedbacktable()
        obj.name=name
        obj.email=email
        obj.age=age
        obj.dining=role
        obj.recommend=userrecommend
        obj.favorite=mostLike
        obj.improve=prefer
        obj.comment=comment
        obj.save()
        mydata=feedbacktable.objects.all()
        return redirect("Feedback")
    return render(request,"Feedback.html")


    
    
def Booking(request):
    mydata=bookingtable.objects.all()
    if(mydata!=""):
        return render(request,"Booking.html",{"bookingtable":mydata})
    else:
        return render(request,"Booking.html")

def bookingdata(request):
    if request.method == "POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        date=request.POST["date"]
        time=request.POST["time"]
        counts=request.POST["counts"]
        additional=request.POST["additional"]

        obj=bookingtable()
        obj.firstname=firstname
        obj.lastname=lastname
        obj.email=email
        obj.phone=phone
        obj.date=date
        obj.time=time
        obj.counts=counts
        obj.additional=additional
        obj.save()
        mydata=bookingtable.objects.all()
        return redirect("Booking")
    return render(request,"Booking.html")

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

def useraccess(request):
    if request.method =="POST":
        name=request.POST['name']
        passwordd=request.POST['passwordd']
       
       
        user=authenticate(username=name,password=passwordd)
        
        if user is not None:
            return render(request,"Booking.html")
        else:
            return redirect("login")
    return render(request,"login.html")

def Register(request):
    template=loader.get_template('Register.html')
    return HttpResponse(template.render())

def adduser(request):
    if request.method == "POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        usname=request.POST['usname']
        psword=request.POST['psword']
        myuser=User.objects.create_user(usname,email,psword)
        myuser.save()
        return redirect("login")
    return render (request,'login.html')






   