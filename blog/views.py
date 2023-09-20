from django.shortcuts import render,HttpResponse
from blog.models import Blog
# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    allblogs=Blog.objects.all()
    context={'blogs':allblogs}
    return render(request,'bloghome.html',context)
def blogpost(request,slug):
    # return HttpResponse(f"this is the {slug}")
    blog=Blog.objects.filter(slug=slug).first()
    context={'blogs':blog}
    return render(request,'blogpost.html',context)
def contact(request):
        return render(request,'contact.html')


