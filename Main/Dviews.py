from django.shortcuts import render,redirect
from django.http import JsonResponse 
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404,get_list_or_404
from .models import Question,Answer,Comment
from .filter import *
from .forms import QuestionForm,QuestionForm2,AnswerForm,CommentForm
import datetime as dt
from django.db.models import Q
from django.utils import timezone

def DeleteQuestion(request,slug):
    if Question.objects.get(slug=slug):
        question = Question.objects.get(slug=slug)
        if request.user == question.author:
            question.delete()
        return redirect('main:home')
    else:
        return redirect('main:home')
def DeleteAnswer(request,id):
    if Answer.objects.get(id=id):
        answer = Answer.objects.get(id=id)
        if request.user == answer.user or request.user == answer.question.author:
            answer.delete()
        return redirect('main:List',id=answer.question.slug )
    else:
        return redirect('main:home')
def deleteComment(request,id):
    if Comment.objects.get(id=id):
        answer = Comment.objects.get(id=id)
        if request.user == answer.user or request.user == answer.link.user or answer.link.question.author:
            answer.delete()
        return redirect('main:List',id=answer.link.question.slug )
    else:
        return redirect('main:home' )
