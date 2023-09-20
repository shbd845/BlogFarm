from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact
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


