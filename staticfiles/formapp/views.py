from django.shortcuts import render
from .models import form_details

# Create your views here.

def index(request):
    return render(request,"base.html")