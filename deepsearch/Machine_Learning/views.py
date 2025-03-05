from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    return HttpResponse('<h1>Machine Learning</h1>')

def about(request):
    return HttpResponse('<h1>🤖 Machine Learning</h1> <p>Our Django-based Machine Learning project leverages predictive modeling and data-driven insights to solve real-world problems efficiently.</p>')