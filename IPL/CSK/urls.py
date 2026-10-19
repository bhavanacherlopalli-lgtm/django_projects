from CSK.views import*
from django.urls import path
app_name='csk'
urlpatterns=[
    path('captain/',captain,name='captain'),
   ]