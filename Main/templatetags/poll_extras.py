from django import template
from Main.models import *
from django.contrib.auth.models import User
register = template.Library()

@register.filter()
def iltreate_of_num(value):
    return range(1,value)
@register.filter()
def Slug(value):
    return f'id{value}'
@register.filter()
def Class(value):
    return f'class{value}'

@register.filter()
def LikeClass(value):
    return f"like{value}"

@register.filter()
def hidClass(value):
    return f"hid{value}"

@register.filter()
def hidClass2(value):
    return f"hid2{value}"

@register.filter()
def filterAnswer(value):
    if value:
        return Answer.objects.filter(question=value).count()
    else:
        return ""
@register.filter()
def CommentAnswer(value):
    if value:
        return Comment.objects.filter(link=value).count()
    else:
        return ""

@register.filter()
def DisClass(value):
    return f"Dis{value}"

@register.filter()
def QuestionFilter(value):
    if value:
        return Question.objects.filter(author=value).count()

@register.filter()
def AnswerFilter2(value):
    if value:
        return Answer.objects.filter(user=value).count()

@register.filter()
def clearimg(value):
    if value:
       return value.replace('<img ',"'<img style='display:none;'")

@register.filter()
def DisrFilter2(value):
    if value:
        return Answer.objects.filter(question=value).count()
