from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,"home.html")
def whoweare(request):
    return render(request,"test.html")
def migration(request):
    return render(request,"migration1.html")
def career(request):
    return render(request,"career.html")
def helpdesk(request):
    return render(request,"helpdesk.html")

def customersupport(request):
    return render(request,"customersupport.html")
def uiux(request):
    return render(request,"uiux.html")
def website(request):
    return render(request,"website.html")

def forge(request):
    return render(request,"forge.html")