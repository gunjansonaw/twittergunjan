from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import tweepy


def index(request):
    return render(request,'index.html')

def twitter(request):
    pass

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')    
        pass2 = request.POST.get('password2')  
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exists")
            return redirect('index')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
        
        if len(username)>10:
            messages.error(request,"Username must be under 10 charecters")
            
        if pass1 != pass2:
            messages.error(request,"Password didn't match")
        
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('index')
            

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('signin')
    
    return render(request, "signup.html")



def signin(request):
    if request.method == 'POST':
        username=request.POST.get('user')
        password=request.POST.get('pass1')
        user=authenticate(username=username,pass1=password)
        fname=fname
        if user is not None:
            login(request,user)
            return render(request,'gallery.html')
            
        else:
            messages.error(request,"Invalid Credentials")
            return redirect ('index')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return render(index)
