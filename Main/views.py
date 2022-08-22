from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import JsonResponse,Http404
from django.template.loader import render_to_string
from .models import Question,Answer,Comment
from Profile.models import Profile
from .filter import *
from .forms import QuestionForm,QuestionForm2,AnswerForm,CommentForm
import datetime as dt
from django.db.models import Q
from django.utils import timezone
from Main.extra2  import extra
import DateTime as dts
from asgiref.sync import sync_to_async
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.core import serializers
import json
# Create your views here.
def home(request):
    question =Question.objects.all()
    cont=ModelFilter(request.GET,queryset=Question.objects.all())
    if request.GET.get("title"):
        question = cont.qs
    paginator = Paginator(question,7)
    page_number = request.GET.get('page')
    try:
       current_page= paginator.page(page_number)
       question = paginator.page(page_number).object_list
    except PageNotAnInteger:
        current_page= paginator.page(1)
        question = paginator.page(1).object_list
    except EmptyPage:
        question = paginator.page(paginator.num_pages).object_list
        raise Http404
    querysets =User
    if request.is_ajax():
        main=int(request.GET.get('url'))
        data={"has_previous":paginator.page(main).has_previous(),"has_next":paginator.page(main).has_next()}
        list_of_question =paginator.page(main).object_list
        Json_data =serializers.serialize("json",list_of_question)
        Json_user =serializers.serialize("json",Profile.objects.all())
        Json_state = json.dumps(data)
        return JsonResponse(data={'all':Json_data,'user':Json_user,"states":Json_state,"current_page":paginator.page(main).number,"all_page":paginator.num_pages})
    try:
        question2 = Question.objects.all().order_by("date")
        popular_question = []
        five = reversed(question2[len(question2)-5:len(question2)])
    except AssertionError:
        five = question
    boom =[querysets.objects.all()[0]]
    for ques in querysets.objects.all():
        if len(boom) > 3 :
            length = -3
        elif len(boom) > 2:
            length = -2
        else:
            length = -1
        if ques.profile.followers.count() >= boom[length].profile.followers.count():
            if ques in boom:
                pass
            else:
                boom.append(ques)
    try:
        fifth =reversed(boom[len(boom)-8:len(boom)])
    except AssertionError:
        fifth =reversed(boom)
    return render(request,'index.html',
    {'form':cont,'all':question,'five':five,'question':Question,'boom':fifth,"paginator":paginator,"current_page":current_page}
    )

def AskQuestion(request):
    Form =QuestionForm()
    Form2 =QuestionForm2()
    if request.method == "POST":
        if request.user.is_authenticated:
            form =QuestionForm(request.POST)
            form2 =QuestionForm2(request.POST)
            if form.is_valid() and form2.is_valid():
                Question.objects.create(author=request.user,question_title=form.cleaned_data.get('question_title'),description=form2.cleaned_data.get('description'))
                return redirect('main:home')
            else:
                messag = ''
                messag2 = ''
                if not form2.is_valid():
                    messag ="<style>.desc{border:1px solid red;}</style>"
                    messag2 ='empty value'
                return render(request,'Question.html',{'form':form,'form2':form2,'messag':messag,'messag2':messag2})
        else:
            messages.success(request,'Your are not signed in')
    return render(request,'Question.html',{'form':Form,'form2':Form2})

def QuestionView(request,id):
    question =get_object_or_404(Question, slug=id)
    ques=Question.objects.get(slug=id)
    answer =Answer.objects.filter(question=question)
    froms =CommentForm()
    Form =AnswerForm()
    return render(request,'ViewQuestion.html',{'ques':question,'anws':answer,"form":Form,'forms':froms})
def AskAnswer(request, slug ):
    question =get_object_or_404(Question,slug=slug )
    answer =Answer.objects.filter(question=question)
    if request.method == 'POST':
        form =AnswerForm(request.POST)
        if form.is_valid():
            Answer.objects.create(user=request.user,question=question,Answer=form.cleaned_data.get('Answer'))
            if answer.count() == 1:
                question.answered = True
                question.save()
            return redirect('main:List',id=slug)
        else:
            return redirect('main:List' ,id=slug)
def comment(request):
    if request.is_ajax():
        if request.method == "POST":
            for anl in Answer.objects.all():
                if request.POST.get(str(anl.id)):
                    lons = request.POST.get(f'comm{anl.id}')
                    ans =Answer.objects.filter(id=lons).first()
                    long =request.POST.get(str(anl.id))
            Comment.objects.create(user=request.user,link=ans,comment=long)
    return JsonResponse({'form':'hello'})
def LIke(request):
    if request.is_ajax():
        if request.method == "POST":
            for anw in Answer.objects.all():
                ser ='hid' + str(anw.id)
                if request.POST.get(ser):
                    long =request.POST.get(ser)
                    ans =Answer.objects.get(id=long)
            if request.user in ans.likes.all():
                ans.likes.remove(request.user)
            elif not request.user in ans.likes.all():
                ans.likes.add(request.user)
        return JsonResponse({'form':'hello'})
def DIslike(request):
    if request.is_ajax():
        if request.method == "POST":
            for anw in Answer.objects.all():
                ser ='hid2' + str(anw.id)
                if request.POST.get(ser):
                    long =request.POST.get(ser)
                    ans =Answer.objects.get(id=long)
            if request.user in ans.dislike.all():
                ans.dislike.remove(request.user)
            elif not request.user in ans.dislike.all():
                ans.dislike.add(request.user)
        return JsonResponse({'form':'hello'})
def add_view(request, slug):
    if request.is_ajax():
        question = Question.objects.get(slug=slug)
        question.views += 1
        question.save()
        print(question.views)
        return JsonResponse({'res':question.views})