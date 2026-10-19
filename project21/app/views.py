from django.shortcuts import render
from app.views import*
# Create your views here.


def insert_webpages(request):
    EWFO=webpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=webpageForm(request,POST)
        if WFDO.is_valid():
            TO=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            TWO=webpage.objects.get_or_create(topic_name=TO,name=name,url=url)
            if TWO[1]:
                return HttpResponse('webpage is created')
            else:
                return HttpResponse('Already Exist')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_webpages.html',d)




def insert_webpages_mf(request):
    EWMFO=webpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=webpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_webpages_mf.html')



def insert_webpages(request):
    EWMFO=webpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=webpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Created')

