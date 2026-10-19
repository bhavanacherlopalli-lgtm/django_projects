from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True,)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100,null=True,blank=True)
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True,)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField(null=True,blank=True)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    comm=models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mobile=models.CharField(default='9515497711')

class SalGrade(models.Model):
    grade=models.CharField(primary_key=True,max_length=100)
    losal=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hisal=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    


