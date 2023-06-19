from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")


def form(request):

    if request.method == 'POST':
        print('okkkkkkkk444')
        name = request.POST.get('name')
        dob =  request.POST.get('dob')
        age =   request.POST.get('age')
        gender = request.POST.get('gender')
        phno = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        address =request.POST.get('address')
        district = request.POST.get('district')
        branch =  request.POST.get('branch')
        account =  request.POST.get('account')
        materials =  request.POST.get('materials')
        print(materials)
        abc= Form.objects.create(name=name,dob=dob,age=age,gender=gender,phno=phno,email=email,address=address,district=district,branch=branch,account=account,materials=materials)
        if abc:
         messages.info(request,'Data inserted Succesfully')
         return redirect('home')

    return render(request, "form.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")
