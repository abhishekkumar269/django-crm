from django.shortcuts import render,redirect
from django.contrib.auth import login , logout ,authenticate
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    # check to see if loggin in

    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

            #aunticate
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Hello world")

            return redirect('home')
        
        else :
            messages.success(request,"please enter correct info")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

# def login_user(request):
#     # return render(request,'login.html',{})
#     pass


def logout_user(request):
    # return render(request,'logut.html',{})
    logout(request)
    messages.success(request,"You have sucessfully logout...")
    return redirect('home')
    
def register_user(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid ():
            form.save()
            #authentic and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'you have sucessfully resgister...')
            return redirect('home')
        
    else :
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
    # lookup records
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    else :
        messages.success(request,"you must be logged in ")
        return redirect('home')


def delete_record(request,pk):  
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"You have sucessfully Delete Record...")
        return redirect('home')
    else:
        messages.success(request,"Kindly login your account ...")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None )
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Recored added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request,"You must be logged in...")
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()

            messages.success(request,"Record is updated sucessfully...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})

    else:
        messages.success(request,"You must be logged in...")
        return redirect('home')
    


    






    
