from instamart.views import*
from django.urls import path
app_name='instamart_app'
urlpatterns=[
    path('chocolate/',chocolate,name='chocolate'),
    path('icecream/',icecream,name='Icecream'),
]