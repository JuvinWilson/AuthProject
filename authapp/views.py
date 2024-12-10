from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def login1(request):
    return render(request,'login.html')

def adminhome(request):
    return render(request,'adminhome.html')
@login_required(login_url='login1')
def about(request):
    # session
    # if 'userid' in request.session:
    #     return render(request,'about.html')
    # else:
    #     return render(request,'login.html')

    # is_authenticated method

    # if request.user.is_authenticated:
    #     return render(request,'about.html')
    # else:
    #     return render(request,'login.html')

    return render(request,'about.html')


def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        p_password = request.POST.get('pwd')
        c_password = request.POST.get('repwd')
        email=request.POST.get('email')
        if p_password == c_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"User Already Exists")
                return redirect('signup')
            else:
                uobj = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=p_password)
                uobj.save()
        else:
            messages.info(request,"password doesnot match")
            return redirect('signup')
        return redirect('login1')
    return render(request,'signup.html')

def loginauth(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            # request.session['userid']=user.id
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request,user)
                messages.info(request,f'welcome {username}')
                return redirect('about')
        else:
            messages.info(request,"invalid username and password")
            return redirect('login1')
    return render(request,'login.html')

def logout(request):
    # request.session['userid']=''
    # if request.user.is_authenticated:
    auth.logout(request)
    return redirect('home')

