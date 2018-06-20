from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import kyaUser
def sign_up(request):
    if request.method=="POST":
        form=kyaUser(request.POST)
        if form.is_valid():
            u_n=form.cleaned_data["u_n"]
            p=form.cleaned_data["p1"]
            print(u_n,p)
            user=User.objects.create_user(username=u_n,password=p)
    else:
        form=kyaUser()
    return render(request,'account/sign_up.html',{'form':form})
def log_in(request):


    return render(request,'account/log_in.html')
