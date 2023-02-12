from django.shortcuts import render, redirect
from goodcauses.models import Signin, Profile, Feedback, Funds
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = authenticate(email = email,password = password)
        print(user)
        if user:
            # login(request,user)
            return render(request,'dash.html')
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        type = request.POST.get("type")
        password = request.POST.get("password")
        ins = Signin(name = name,email = email,type = type,password = password)
        ins.save()
    return render(request, 'signup.html')

def list(request):
    list = Profile.objects.all()
    name = Signin.objects.all()
    context = {'list' : list, 'name' : name}
    return render(request, 'list.html',context)

def profile(request):
    if request.method == 'POST':
        orgname = request.POST['orgname']
        phone = request.POST["phone"]
        previouswork = request.POST["previouswork"]
        futuregoals = request.POST["futuregoals"]
        fundingneeds = request.POST["fundingneeds"]
        files = request.FILES.get("files")
        ins = Profile(orgname=orgname, phone=phone, previouswork=previouswork, futuregoals=futuregoals,fundingneeds=fundingneeds, files=files)
        ins.save()
    return render(request, 'profile.html')

def fundraising(request):
    if request.method == 'POST':
        frname = request.POST['frname']
        frphone = request.POST["frphone"]
        eventdesc = request.POST["eventdesc"]
        funds = request.POST["funds"]
        documents = request.FILES.get("document")
        ins = Funds(frname=frname, frphone=frphone, eventdesc=eventdesc, funds=funds, documents=documents)
        ins.save()
    return render(request, 'fundraising.html')

def dash(request):
    return render(request, 'dashboard.html')

def feedback(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        femail = request.POST.get("femail")
        country = request.POST.get("country")
        desc = request.POST.get("desc")
        ins = Feedback(fname = fname,femail = femail,country = country,desc = desc)
        ins.save()
    return render(request, 'feedback.html')