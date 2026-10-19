from django import forms

from django.core.validators import RegexValidator,MinimumLengthValidator




class NameForm(forms.Form):
    name=forms.CharField(validators=[MinimumLengthValidator(5)])
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.passwordInput)
    address=forms.CharField()
    gender=forms.ChoiceField(choices=[('MALE','male'),('FEMALE','female')])


    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.validationError('bot has catched')


    