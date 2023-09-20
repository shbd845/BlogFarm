from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact,Member
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    allblogs=Blog.objects.all()
    context={'blogs':allblogs}
    return render(request,'bloghome.html',context)
def blogdetail(request,slug):
    # return HttpResponse(f"this is the {slug}")
    blog=Blog.objects.filter(slug=slug).first()
    context={'blogs':blog}
    return render(request,'blog.html',context)
def contact(request):
        context={"success":False}
        if request.method=="POST":
             name=request.POST.get("name")
             email=request.POST.get("email")
             query=request.POST.get("query")
             instance= Contact(name=name,email=email,query=query)
             instance.save()
             context={"success":True}
        
        return render(request,'contact.html',context)
def addblog(request):
    context={"successs":False}
    if request.method=="POST":
             title=request.POST.get("title")
             content=request.POST.get("content")
             slug=request.POST.get("slug")
             instance= Blog(title=title,content=content,slug=slug)
             instance.save()
             context={"success":True}
    return render(request,'addblog.html',context)

def login(request):
     context={"success":False}
     if request.method=="POST":
             username=request.POST.get("username")
             email=request.POST.get("email")
             pwd=request.POST.get("password")
             user = authenticate(username=username, password=pwd)
             if user is not None:
                   context={"success":"true"}
             else:
                   context={"success":"error"}
             
     return render(request,'login.html',context)

def signup(request):
     context={"success":False}
     if request.method=="POST":
             firstname=request.POST.get("firstname")
             lastname=request.POST.get("lastname")
             username=request.POST.get("username")
             email=request.POST.get("email")
             pwd=request.POST.get("password")
             user = User.objects.create_user(username,email,pwd)
             user.first_name=firstname
             user.last_name=lastname
             user.save()
             context={"success":True}
     return render(request,'signup.html',context)

