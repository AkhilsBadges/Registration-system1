from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        usr=authenticate(request,username=uname,password=pass1)
        if usr is not None:
            login(request,usr)
            return redirect('home')
        elif not uname or not pass1:
            return HttpResponse("Please fill in all the fields.")
        else:
            return HttpResponse("Incorrect Details!!")




    return render(request,'login.html')

def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if not uname or not email or not pass1 or not pass2:
            return HttpResponse("Please fill in all the fields.")
        
        if pass1!=pass2:
            return HttpResponse("Incorrect password!!")
        else:
            new_user=User.objects.create_user(uname,email,pass1)
            new_user.save()
            return redirect('login')
        
    return render(request,'signup.html')


def Logout(request):
    logout(request)
    return redirect('login')