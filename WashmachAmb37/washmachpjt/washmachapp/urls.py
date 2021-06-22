from  django.urls import path

from .views import login

app_name = 'washmachapp'

urlpatterns = [
  
    path('',login,name='login'), 
]