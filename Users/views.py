from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .forms import Register,LoginForm
# Create your views here.


def SignUp(request):
    signup =Register()
    if request.method == 'POST':
        signu =Register(request.POST)
        if signu.is_valid():
            user = User.objects.create_user(username=signu.cleaned_data['username'],password=signu.cleaned_data['password1'],email=signu.cleaned_data['email'])
            loger =auth.authenticate(user=signu.cleaned_data['username'],password=signu.cleaned_data['password1'])
            auth.login(loger)
            return redirect('main:home')
        else:
            return render(request,'signup.html',{'ss':signu})
    return render(request,'signup.html',{'ss':signup})

def login(request):
    forms=LoginForm()
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            users =auth.authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if users is not None:
                auth.login(request,users)
                return redirect('main:home')
            else:
                return redirect('main:home')
        else:
            return render(request,'login.html',{'form':form})

    return render(request,'login.html',{'form':forms})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('main:home')
