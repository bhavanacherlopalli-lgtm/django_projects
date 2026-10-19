from django.db import models

# Create your models here.
from app.models import*
class Details(models.Model):
    Name=models.CharField(primary_key=True)
    Url=models.URLField()
    Age=models.IntegerField()
    Password=models.CharField()
