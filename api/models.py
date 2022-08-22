from django.db import models

# Create your models here.
class TESTModel(models.Model):
    title =models.CharField(max_length=23)
    text=models.TextField(blank=True,null=True)