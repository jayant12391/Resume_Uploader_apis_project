from django.db import models



STATE_CHOICES = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),("Gujarat","Gujarat"),
    ("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),
    ("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra")
                 )

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    dob = models.DateTimeField(auto_now=False , auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICES , max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)

    