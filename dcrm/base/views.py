from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django. contrib import messages
from.forms import SignUpForm, AddRecordForm

from . models import Record

def home(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, "home.html", {'records':records})
    else:
        messages.info(request, "You must login to view this page...")
        return redirect("login")






def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("home")
        
        else:
            messages.warning(request, "username or password is incorrect!!")
            return redirect("login")
    else:
        return render(request, "login.html")
    
    
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("home")
        else:
            form = SignUpForm()
            messages.error(request, "An error occured during registration. Try again")
            return render(request, "register.html",  {'form':form})
        
    return render(request, "register.html")

def cust_rec(request, pk):
    if request.user.is_authenticated:
        cust_record = Record.objects.get(id=pk)
        return render(request, "record.html", {'cust_record':cust_record})
    else:
        messages.error(request, "You must be logged in to access this page!")
        return redirect("login") 
    
def delete_cust(request, pk):
    if request.user.is_authenticated:
        del_it=Record.objects.get(id=pk)
        del_it.delete()
        messages.success(request, "Record deleted successfully!") 
        return redirect("home")
    else:
        messages.warning(request, "You must be logged in in order to perform this action!!")
        return redirect("login")
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record added successfully.....")
                return redirect("home")
        return render(request, "add_record.html", {'form':form})
    else:
        messages.error(request, "This page is restricted to only logged in users ")
        return redirect("login")

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully.....")
            return redirect("home")    
        return render(request, "update_record.html", {'form':form})
    else:
        messages.error(request, "Record update can only be done by logged in users!!")
        return redirect("login")
    
    
 
    


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect("home")
