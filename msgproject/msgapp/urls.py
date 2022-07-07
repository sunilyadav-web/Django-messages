from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('send-data/',receiveData,name='send-dta'),
]
