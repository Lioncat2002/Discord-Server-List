from django.shortcuts import render
from django.http import  HttpResponse

from . import models

def HomeView(request):
    guild=models.ServerModel.objects.all()
    context={'guilds':guild}
    return render(request,'baseapp/home.html',context)
