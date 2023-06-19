from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phno = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    account = models.CharField(max_length=250)
    materials = models.CharField(max_length=250)
    def __str__(self):
        return self.name
