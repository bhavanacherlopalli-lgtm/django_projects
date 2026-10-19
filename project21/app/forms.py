from django import forms

from app.models import*

class webpageForm(forms.Form):
    topic_name=CharField(queryset=topics.objects.all())
    name=forms.CharField()
    url=forms.URLField()

class webpageModelForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['url']
        #widgets={'topic_name':forms.RadioSelect}

