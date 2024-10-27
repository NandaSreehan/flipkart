from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    res=User.objects.all()
    a=request.POST.get('n')
    for i in res:
        if i==a:
            return render(request,'home.html',{'i':i})
    return render(request,'home.html',{'res':res})

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def post(request):
    return render(request,'post.html')


##def home(request):
#    return render(request,)
