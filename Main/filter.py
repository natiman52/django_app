import django_filters
from django_filters import CharFilter
from django.forms import TextInput

from .models import Question



class ModelFilter(django_filters.FilterSet):
    title = CharFilter(field_name='question_title',lookup_expr='icontains',label='',widget=TextInput(attrs={'placeholder':'search','class':'form-control mr-sm-2','id':'full2'}))
    class Meta:
        model = Question
        fields =[]