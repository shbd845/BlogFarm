from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'bloghome.html')
def blogpost(request,slug):
    # return HttpResponse(f"this is the {slug}")
    return render(request,'blogpost.html')
def contact(request):
        return render(request,'contact.html')


