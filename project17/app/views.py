from django.shortcuts import render
from django.http import HttpResponse
from app.models import*

# Create your views here.
def insert_topic(request):
    tn = input('Enter ur tn')
    TTO = Topic.objects.get_or_create(topic_name=tn)

    if TTO[1]:
        return HttpResponse('New topic is created')
    else:
        return HttpResponse('Topic is present')

def insert_webpage(request):
    print('available topics are')
    for to in Topic.objects.all():
        print(to.topic_name)
    tn=input('enter ur topic')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        name=input('enter ur name')
        url=input('enter ur url')
        email=input('enter ur email')
        mobile=input('enter ur mobile')
        TUWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email,mobile=mobile)
        if TUWO[1]:
            return HttpResponse('New webpage is created')
        else:
            return HttpResponse('Present')
    else:
        return HttpResponse('Given topic is not present')



def select_multiple(request):
    QSLTO=Topic.objects.all()
    d={'QSLTO':QSLTO}
    if request.method=='POST':
        topics=request.POST.getlist('topics')
        print(topics)
        QSLWO=Webpage.objects.none()
        for topic in topics:
            QSLWO