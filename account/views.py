from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import kyaUser
def sign_up(request):
    if request.method=="POST":
        form=kyaUser(request.POST)
        if form.is_valid():
            u_n=form.cleaned_data["u_n"]
            p=form.cleaned_data["p1"]

            user=User.objects.create_user(username=u_n,password=p)
    else:
        form=kyaUser()
    return render(request,'account/sign_up.html',{'form':form})
def log_in(request):
    if request.method=="POST":
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
    return render(request,'account/log_in.html')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
