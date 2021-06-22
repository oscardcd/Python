from django.http import request
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone

# Create your views here.
def login(request):
        return render(request,'views/login.html')