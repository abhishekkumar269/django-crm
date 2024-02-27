from django.shortcuts import render,redirect
from django.contrib.auth import login , logout ,authenticate
from django.contrib import messages


# Create your views here.

def home(request):
    # check to see if loggin in

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
        return render(request,'home.html',{})


# def login_user(request):
#     # return render(request,'login.html',{})
#     pass


def logout_user(request):
    # return render(request,'logut.html',{})
    logout(request)
    messages.success(request,"You have sucessfully logout...")
    return redirect('home')
    
def register_user(request):
    return render(request,'register.html',{})
    