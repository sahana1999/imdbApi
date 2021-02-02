from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def morning(request):
    return render(request,'testapp/demo.html')
