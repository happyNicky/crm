from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages
from .form import SingUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you are logged in successfully!')
            return redirect('home')
        else:
            messages.success(request,'something went wrong pleas try again...')
            return redirect('home')
    else:
     records=Record.objects.all()
     return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,'you have been logged out!')
    return redirect('home')


def register_user(request):
    if request.method =='POST':
        form=SingUpForm(request.POST)
        if form.is_valid():
            print('the form is valid')
            form.save()
            username =form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request, user)
            messages.success(request,'your are logged in successfully!')
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})
    else:
        form=SingUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{})


def record_user(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else:
        messages.error(request,'you must be logged in to view this page!')
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request,'record deleted successfully!')
        return redirect('home')
    else:
        messages.error(request,'you must be logged in to delete a record')
        return redirect('home')


def add_record(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            form=AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'record added successfully!')
                return redirect('home')
        else:
            form=AddRecordForm()
            return render(request,'add_record.html',{'form':form})

    else:
        messages.error(request,'you must be logged in to add record!')
        return redirect('home')

def update_record(request,pk):
        if request.user.is_authenticated:
            customer=Record.objects.get(id=pk)
            print(customer.first_name)
            if request.method == "POST":
               form=AddRecordForm(request.POST or None,instance=customer)
               if form.is_valid():
                   form.save()
                   messages.success(request,'record updated successfully!')
               return redirect('home')
            else:
                form=AddRecordForm(instance=customer)
            return render(request,'add_record.html',{'form':form})
        else:
            messages.error(request,'you must be logged in to update a record!')
            return redirect('home')





