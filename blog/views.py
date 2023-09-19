from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello")
def blog(request):
    return HttpResponse("blog")
def blogpost(request,slug):
    return HttpResponse(f"this is the {slug}")
def contact(request):
    return HttpResponse("contact")

