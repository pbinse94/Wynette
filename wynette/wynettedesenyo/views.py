from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'wynettedesenyo/index.html'
    return render(request, template, {})

def services(request):
    template = 'wynettedesenyo/services.html'
    return render(request, template, {})