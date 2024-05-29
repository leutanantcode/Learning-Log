from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def Get_all_entry(request):
    all_entry = models.Entry.objects.all()
    return HttpResponse(all_entry)

