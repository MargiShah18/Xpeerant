
from django.shortcuts import render
from .models import Contact,CROUSAL,ac,speciality,contactdetails,logos
def home(request):
    menus=[
        {'id': 1, 'name': 'home','link' : 'home'},
        {'id': 2, 'name': 'About Us', 'link': 'aboutus'},
        {'id': 3, 'name': 'Contractors', 'link': 'contractors'},
    ]
    crousal = CROUSAL.objects.all()
    print(crousal)
    nSlides = len(crousal)
    about=ac.objects.all()
    spec=speciality.objects.all()
    condetails=contactdetails.objects.all()
    log=logos.objects.all()
    params = {'no_of_slides': nSlides, 'range': range(0, nSlides), 'crousal': crousal, 'about': about, 'spec':spec, 'condetails':condetails, 'log':log}
    return render(request, 'base/home.html', params)

    def home(request):
        return render(request,'base/home.html',{})

def aboutUs(request):
    return render(request,'base/aboutus.html',{})

def contractors(request):
    return render(request,'base/contractors.html',{})

def jobrequiremnets(request):
    return render(request, 'base/jobrequirements.html', {})

def clients(request):
    return render(request, 'base/client.html', {})


def stafflogin(request):
    return render(request, 'base/stafflogin.html', {})

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "base/contactus.html")

