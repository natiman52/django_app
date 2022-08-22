from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
import uuid
from django.db.models.signals import post_save
from django.utils.text import slugify
import datetime
import DateTime
from django.dispatch import receiver
from django.db.models.signals import pre_save
import ethiopian_date
# Create your models here.

date = DateTime.DateTime()
class Question(models.Model):
    author = models.ForeignKey(default=1, to=User,on_delete=models.CASCADE)
    question_title = models.CharField(max_length=50,verbose_name='ርዕስ',unique=True)
    description =RichTextUploadingField(verbose_name='ጥያቄ')
    date =models.DateField(default=ethiopian_date.EthiopianDateConverter.to_ethiopian(date.year(),date.month(),date.day()))
    answered=models.BooleanField(default=False)
    slug =models.SlugField(blank=True)
    views =models.IntegerField(blank=True,default=0)
    class Meta:
        ordering=["-date"]
    def __str__(self):
        return self.question_title

class Answer(models.Model):
    user =models.ForeignKey(to=User,on_delete=models.CASCADE,default='1',related_name='creater')
    question =models.ForeignKey(to=Question,related_name='question',default='1',on_delete=models.CASCADE)
    Answer =RichTextField(config_name='Nati',verbose_name='መልስ')
    date = models.DateField(default=ethiopian_date.EthiopianDateConverter.to_ethiopian(date.year(),date.month(),date.day()))
    likes =models.ManyToManyField(to=User,related_name='likes',blank=True)
    dislike =models.ManyToManyField(to=User,related_name='dislike',blank=True)

    def __int__(self):
        return self.id

    def GetComment(self):
        com =Comment.objects.filter(link=self)
        return com
    def GetCount(self):
        com =Comment.objects.filter(link=self).count()
        return com

class Comment(models.Model):
    user =models.ForeignKey(to=User,default="1" ,on_delete=models.CASCADE)
    link =models.ForeignKey(Answer,default="1" , related_name='links', on_delete=models.CASCADE)
    comment =models.CharField(max_length=200)
    date = models.DateField(default=ethiopian_date.EthiopianDateConverter.to_ethiopian(date.year(),date.month(),date.day() ))

@receiver(pre_save, sender=Question)
def save(instance, *args, **kwargs):
    seld =instance
    if not seld.slug:
        seld.slug = slugify(seld.question_title)
