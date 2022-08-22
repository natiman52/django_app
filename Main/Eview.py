from .models import Answer,Question,Comment
from django.shortcuts import render , redirect,get_object_or_404,get_list_or_404
from .forms import QuestionForm2,AnswerForm,CommentForm


def UpdateQuestion(request,slug):
	objects = get_object_or_404(Question, slug=slug)
	form = QuestionForm2(initial={'description':objects.description})
	if request.method == "POST":
		form = QuestionForm2(request.POST)
		if form.is_valid():
			if form.has_changed():
				desc = form.cleaned_data.get('description')
				ques =Question.objects.filter(slug=slug).first()
				ques.description = desc
				ques.save()
				return redirect('main:List', id=slug )
			else:
				return redirect('main:List', id=slug )
		else:
			return render(request,'edit.html',{'form':form})
	return render(request,'edit.html',{'form':form})

def UpdateAnswer(request,id):
	objects = get_object_or_404(Answer,id=id )
	form = AnswerForm(initial={'Answer':objects.Answer})
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			if form.has_changed():
				ans =form.cleaned_data.get('Answer')
				answer =Answer.objects.filter(id=id).first()
				answer.Answer = ans
				answer.save()
				return redirect('main:List', id=answer.question.slug )
			else:
				return redirect('main:List', id=answer.question.slug )
		else:
			return render(request,'edit2.html',{'form':form})
	return render(request,'edit2.html',{'form':form})
