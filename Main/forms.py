from django import forms
from .models import Question,Answer,Comment

class QuestionForm(forms.ModelForm):

    class Meta:
        model =Question
        fields = ['question_title']
    
    def clean_question_title(self):
        question_title =self.cleaned_data.get('question_title')
        r=Question.objects.filter(question_title=question_title)
        B =r.first()
        if r.count():
            raise forms.ValidationError('ይሄ ርዕስ ተወስዷል ሌላ ርዕስ ይምረጡ')
        return question_title

class QuestionForm2(forms.ModelForm):

    class Meta:
        model =Question
        fields =['description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model =Answer
        fields = ['Answer']

class CommentForm(forms.ModelForm):
    comment =forms.CharField(max_length=200,widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model =Comment
        fields = ['comment']