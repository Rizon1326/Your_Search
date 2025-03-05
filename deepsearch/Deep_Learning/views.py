from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def deep_learning(request):
    return HttpResponse('<h1>Deep learning is a subset of machine learning that uses deep neural networks to automatically learn patterns from large amounts of data for tasks like image recognition, NLP, and automation. 🚀</h1>')

def about(request):
    return HttpResponse('<h1>🧠 Deep Learning</h1><p>This Django-powered Deep Learning project utilizes neural networks to automate complex tasks like image recognition and natural language processing.</p>')