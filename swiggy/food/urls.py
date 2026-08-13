from food.views import*
from django.urls import path
app_name='food_app'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani'),
]