from django.urls import path
from .views import home, contactus, aboutUs,contractors,jobrequiremnets,clients,stafflogin

urlpatterns =[
    path('',home,name="home"),
    path('aboutUs/',aboutUs, name="aboutus"),
    path('contractors/',contractors, name="contractors"),
    path('JobRequiremnets/',jobrequiremnets, name="jobrequiremnets"),
    path('Clients/',clients, name="clients"),
    path('contactus/', contactus, name="contactus"),
    path('stafflogin/',stafflogin, name="stafflogin"),
]
