from instamart.views import*
from django.urls import path
app_name='food_app'
urlpatterns=[
    path('chocolate/',chocolate,name='chocolate'),
    path('Icecream/',Icecream,name='Icecream'),
]