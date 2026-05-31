from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect('login')  # FIXED

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  # FIXED

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')
def logout(request):
 if request.method=='GET':
     return redirect('home')
def Collections(request):
    if request.method=='GET':
        return render(request,'Collections.html')
def trendings(request):
    if request.method=='GET':
        return render(request,'trendings.html')
def cart(request):
    return render(request,'cart.html')

def Account(request):
    if request.method=='GET':
        return render(request,'Account.html') 
def contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
def about(request):
    if request.method=='GET':
        return render(request,'about.html') 
def Completetransaction(request):
    if request.method=='GET':
        return render(request,'Completetransaction.html')
