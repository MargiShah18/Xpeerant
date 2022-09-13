from django.contrib import admin

# Register your models here.
from .models import Contact,CROUSAL,ac,speciality,contactdetails,logos

admin.site.register(Contact)
admin.site.register(CROUSAL)
admin.site.register(ac)
admin.site.register(speciality)
admin.site.register(contactdetails)
admin.site.register(logos)