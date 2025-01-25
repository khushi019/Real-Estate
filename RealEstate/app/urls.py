from django.urls import path
from app.views import *

urlpatterns=[
    path('',predict,name='prediction'),
]