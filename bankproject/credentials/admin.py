from django.contrib import admin
from .models import Form

# Register your models here.



class FormModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age','gender','phno','email','address','district','branch')

admin.site.register(Form, FormModelAdmin)