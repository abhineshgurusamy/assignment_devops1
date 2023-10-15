from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def indexhtml1(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def indexhtml2(request):
    template = loader.get_template('task.html')
    return HttpResponse(template.render())
    