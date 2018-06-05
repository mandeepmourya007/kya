from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def sign_up(request):

    userform=UserCreationForm()
    return render(request,'account/sign_up.html',{'form':userform})
