from django.db import models


# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class CROUSAL(models.Model):
    image_id = models.AutoField
    imagename = models.CharField(max_length=50)
    imagetext = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    image = models.ImageField(upload_to="base/images", default="")

    def __str__(self):
        return self.imagename


class ac(models.Model):
    ac_image_id = models.AutoField
    ac_image = models.ImageField(upload_to="base/images", default="")
    ac_title = models.CharField(max_length=50)
    ac_subtitle = models.CharField(max_length=50)
    ac_desc_p1 = models.CharField(max_length=200)
    ac_desc_p2 = models.CharField(max_length=200)
    ac_link = models.CharField(max_length=200)

    def __str__(self):
        return self.ac_title

class speciality(models.Model):
    sp_image_id = models.AutoField
    sp_image = models.ImageField(upload_to="base/images", default="")
    sp_title = models.CharField(max_length=50)
    sp_desc_p1 = models.CharField(max_length=200)
    sp_link = models.CharField(max_length=200)
    link_color = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.sp_title

class contactdetails(models.Model):
    cd_id = models.AutoField
    cd_con1 = models.CharField(max_length=10)
    cd_con2 = models.CharField(max_length=10)
    cd_ceoname= models.CharField(max_length=50)
    cd_ceocon1 = models.CharField(max_length=10)
    cd_ceocon2 = models.CharField(max_length=10)
    cd_ext = models.CharField(max_length=5)
    cd_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.cd_ceoname

class logos(models.Model):
    sp_logo_id = models.AutoField
    sp_logo = models.ImageField(upload_to="base/images", default="")
    sp_logoname = models.CharField(max_length=50)

    def __str__(self):
        return self.sp_logoname
