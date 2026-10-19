from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import Emp,Dept
from django.db.models.functions import*
 


def empToDeptJoin(request):
    QSLEDO=Emp.objects.all().select_related('deptno')
    QSLEDO=Emp.objects.select_related('deptno').all()
    QSLEDO=Emp.objects.filter(sal__gt=5000).select_related('deptno')

    QSLEDO=Emp.objects.filter(sal__gt=60000)
    Emp.objects.values(
    'ename',
    'deptno__dname')

    Emp.objects.values(
    'ename',
    'sal',
    'deptno__dname')

    Emp.objects.values(
    'ename',
    'deptno__dname',
    'deptno__loc')

    Emp.objects.values(
    'ename',
    'deptno__dname',
    'deptno__loc')

    Emp.objects.filter(
    deptno__dname='SALES').values(
    'ename',
    'sal',
    'deptno__dname')

    Emp.objects.filter(
    deptno__loc='DALLAS').values(
    'ename',
    'job',
    'sal',
    'deptno__dname',
    'deptno__loc')

    Emp.objects.filter(
    sal__gt=2000).values(
    'ename',
    'sal',
    'deptno__dname')

    Emp.objects.filter(
    deptno__dname='ACCOUNTING').values(
    'ename',
    'job',
    'sal',
    'deptno__dname')


    Emp.objects.filter(
    sal__range=(2000, 4000)).values(
    'ename',
    'sal',
    'deptno__dname')


    Dept.objects.filter(
    dname='SALES').values(
    'dname',
    'loc',
    'emp__ename',
    'emp__job',
    'emp__sal')

    QSLEDO=Emp.objects.values('ename','mgr__ename')

    QSLEDO=Emp.objects.filter(mgr__isnull=False)

    QSLEDO=Emp.objects.filter(mgr__isnull=True)

    QSLEDO=Emp.objects.filter(mgr__ename='kane')

    QSLEDO=Emp.objects.values(
        'empno',
        'ename',
        'mgr__empno',
        'mgr__ename'
    )



    #d={'QSLEDO':QSLEDO}

    QSLEDO=Emp.objects.exclude(mgr__ename='kane')



    return render(request,'empToDeptJoin.html',d)


def EmpToMgrJoin(request):
    QLEMO=Emp.objects.all().select_related('mgr')
    


    d=('QLEMO':QLEMO)
    return render(request,'EmpToMgrJoin.html')


