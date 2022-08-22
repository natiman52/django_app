from .models import Question,Answer,Comment
import DateTime as dt
import datetime
from django.db.models import Q

def extra(request,question):
    filters1 = None
    filters2 = None
    if request.GET.get('time') == 'on':
        nahom =dt.DateTime() - 30
        time =datetime.date(nahom.year(),nahom.month(),nahom.day()).isoformat()
        filters1 =Question.objects.filter(Q(date__lte=time))
    elif request.GET.get('time2') == 'on':
        na=dt.DateTime()
        tim = datetime.date(na.year(),na.month(),na.day()).isoformat()
        filt=Question.objects.filter(Q(date__lte=tim))
        filters1 = filt
        print(filters1)
    elif request.GET.get('ans1') == 'on':
        quest =Question.objects.filter(answered=True)
        filters2 =quest
    elif request.GET.get('ans2') == 'on':
        quest =Question.objects.filter(answered=False)
        filters2=quest
    elif request.GET.get('all') == 'on':
        filters1 = None
        filters2 = None
    if filters1 == None and filters2 == None:
        return question
    elif filters1 != None and filters2 != None:
        question = filters1
        question += filters2
        return question
    elif filters1 != None:
        question = filters1
        return question
    elif filters2 != None:
        question = filters2
        return question
