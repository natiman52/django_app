from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,m2m_changed,post_delete
from django_resized import ResizedImageField
# Create your models here.



class Profile(models.Model):
    owner =models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic =ResizedImageField(size=[360,400],default='male.jpg',upload_to='profile_pic',verbose_name='መለያ ፎቶ')
    followers =models.ManyToManyField(User,blank=True,related_name='follows')
    bio =models.TextField(blank=True,verbose_name='ባዮ')
    job = models.CharField(max_length=26, blank=True,verbose_name='ስራ')
    telegram =models.CharField(max_length=250,blank=True)
    facebook =models.CharField(max_length=250,blank=True)


    @receiver(post_save,sender=User)
    def post_cald(sender,instance,created,*args,**kwargs):
        if created:
            Profile.objects.create(owner=instance)
            instance.profile.save()

