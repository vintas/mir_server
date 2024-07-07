from django.shortcuts import render
from django.http import HttpResponse
 
 
def index(request):
  return HttpResponse("Hello World")

def getPackageDetails(request):
  return HttpResponse("Hello World2")

def addDependency(request):
  return HttpResponse("Hello World3")
