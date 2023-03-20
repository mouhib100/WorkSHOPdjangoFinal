from django.shortcuts import render
from .forms import *
from django.contrib.auth import login
# Create your views here.

def register(req):
    form = RegisterForm()
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(req, user=user)
            return redirect('EventList')
        else:
            return redirect('register')
        
    return render(req, "", {"form": form})    
