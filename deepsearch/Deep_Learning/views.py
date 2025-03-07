from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def deep_learning(request):
    intro= {'what':'Deep Learning is a subset of Machine Learning that focuses on the development of computer programs that can access data and use it to learn for themselves.'}
    return render(request, 'deep_learning/intro.html',context=intro)
def about(request):
    about={'what':'This Django-powered Deep Learning project utilizes neural networks to automate complex tasks like image recognition and natural language processing.'}
    return render(request, 'deep_learning/about.html',context=about)