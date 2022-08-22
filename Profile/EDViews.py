from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UpdateProfile,UpdateProfile2
from django.contrib.auth.models import User,auth
from .models import Profile
from .forms import UdatePhoto,DeleteForm
from django.http import JsonResponse
from django.contrib import messages
import os
from django.conf import settings
def ProfileEdit(request):
    user = request.user
    profile =request.user.profile
    form1 =UpdateProfile(instance=profile)
    form2 =UpdateProfile2(initial={'username':user.username,'email':user.email})
    if request.method == 'POST':
        form1 =UpdateProfile(request.POST)
        form2 =UpdateProfile2(request.POST)
        if form1.is_valid() and form2.is_valid():
            user.username =form2.cleaned_data['username']
            user.email =form2.cleaned_data['email']
            user.save()
            profile.job =form1.cleaned_data['job']
            profile.facebook =form1.cleaned_data['facebook']
            profile.telegram =form1.cleaned_data['telegram']
            profile.bio =form1.cleaned_data['bio']
            profile.save()
            return redirect('profile')
        else:
            return render(request,'update.html',{'form1':form1,'form2':form2})

    return render(request,'update.html',{'form1':form1,'form2':form2})

def EditPhoto(request):
    user = request.user
    user2 =request.user.profile.profile_pic
    photo = UdatePhoto(request.POST,request.FILES,instance=user.profile)
    if request.is_ajax():
        if photo.is_valid():
            try:
                img = str(user2)
                os.remove(os.path.join(settings.MEDIA_ROOT,img))
            except FileNotFoundError:
                pass
            photo.save()
            return JsonResponse({'helo':"halo"})

def DeleteUser(request):
    user =request.user
    form =DeleteForm()
    if request.method == "POST":
        form2 =DeleteForm(request.POST)
        if form2.is_valid():
            user2 = auth.authenticate(username=user.username,password=form2.cleaned_data['password'])
            if user2:
                user.delete()
                return redirect('main:home')
            if not user2:
                messages.error(request,'sorry your password didn\'t much')
                return render(request,'DeleteUser.html',{'form':form})
    return render(request,'DeleteUser.html',{'form':form})
