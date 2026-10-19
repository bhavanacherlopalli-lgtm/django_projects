from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=100)


class webpage(models.Model):
    topic_name=models.CharField(primary_key=True)
    name=models.CharField()
    url=models.URLField()