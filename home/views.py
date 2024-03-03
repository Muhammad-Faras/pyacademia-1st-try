from django.shortcuts import render,HttpResponse
# Create your views here.

from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'