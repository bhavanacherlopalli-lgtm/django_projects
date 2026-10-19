from django.db import models

# Create your models here.
class Country(models.Model):
    country_id=models.CharField(primary_key=True,max_length=100)
    country_name=models.CharField()

class Capital(models.Model):
    capital_id=models.CharField(primary_key=True,max_length=100)
    capital_name=models.CharField()
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)
    population=models.IntegerField(max_length=100,null=True,blank=True)
