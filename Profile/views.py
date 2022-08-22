from django.shortcuts import render,redirect
from django.http import JsonResponse
from Main.models import Question, Answer
from django.contrib.auth.models import User
from .models import Profile
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UdatePhoto
# Create your views here.

def profile(request):
    question =Question.objects.filter(author=request.user)
    answer =Answer.objects.filter(user=request.user)
    form =UdatePhoto()
    loop = 0
    for ans in answer:
       loop +=ans.likes.all().count()
    return render(request,'profile.html',{'ques':question,'answ':answer,'liker':loop,'form':form})


def show_profile(request,username):
    user =User.objects.filter(username=username).first()
    like_count = 0
    if request.user == user :
        return redirect('profile')
    question =Question.objects.filter(author=user)
    answer =Answer.objects.filter(user=user)
    for ans in answer:
        like_count += ans.likes.count()
    if request.is_ajax():
        data = {
            'data' : request.POST.get('follow1')
        }
        return JsonResponse(data)
    return render(request,'show-profile.html',{'ques':question,'answ':answer,"like_count":like_count,'owner':user})

def Follow(request):
    if request.method == 'POST':
        user = request.user
        owner =User.objects.get(username=request.POST.get('follow'))
        if user in owner.profile.followers.all():
            owner.profile.followers.remove(user)
        elif not user in owner.profile.followers.all():
            owner.profile.followers.add(user)
    if request.is_ajax():
        data =request.POST.get('follow')
        html=render_to_string('show-profile.html',{'owner':data},request=request)
        return JsonResponse({'form':html})
