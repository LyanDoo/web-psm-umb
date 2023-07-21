from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            form = LoginForm()
            message = "Can't Login! Check your username or password"
            return render(request,'./login/loginform.html',{"form":form,"user":request.user,"message":message})
    else :
        form = LoginForm()
    return render(request,'./login/loginform.html',{"form":form,"user":request.user})

def logout_view(request):
    logout(request)
    return redirect("/")