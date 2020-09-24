import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,request.POST.get("email"),request.POST.get("password"))
        if user != None:
            login(request,user)
            return HttpResponseRedirect('/admin_home')
        else:
            return HttpResponse("Invalid Login")

def GetUserDetails(request):
    if request.user!= None:
        return HttpResponse("User: "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/") #redirect to login page