from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=100)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField()
    url=models.URLField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(default='9390866276')
    address=models.CharField(null=True,blank=True)

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField()
    date=models.DateField()
