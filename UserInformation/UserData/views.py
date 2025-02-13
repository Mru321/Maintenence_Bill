from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PersonalInfo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def table(request):
    return render(request, "UserData/table.html")

def signup_view(request):
    if request.method=='POST':

        try:
            username=request.POST['username']
            user1=User.objects.get(username=username)
            return render(request, "UserData/signup.html",{
                'message':'Username already Taken!!'
            })
        except User.DoesNotExist:



            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            user123=User.objects.create_user(username=username, password=password, email=email)
            user123.save()
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            phone=request.POST['phone']
            building=request.POST['building']
            room=request.POST['roomno']
            profile=PersonalInfo(user=user123, first_name=first_name, last_name=last_name, phone=phone, building=building, roomno=room)
            profile.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "UserData/signup.html")
    
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('welcome', kwargs={'username': username}))
        else:
            return render(request, "UserData/login.html", {
                "message":"Invalid Credentials!"
            })
    else:
        return render(request, "UserData/login.html")
    

def welcome(request, username):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signup'))
    else:
        user12=User.objects.get(username=username)
        profile=PersonalInfo.objects.get(user=user12)
        return render(request, "UserData/welcome.html",{
            "profile":profile
        })
    
def logout_view(request):
    logout(request)
    return render(request, "UserData/login.html", {
        "message": "You have logged out!!"
    })
