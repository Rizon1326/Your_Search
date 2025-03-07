from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    means={'what':'Transforming data into intelligence, one algorithm at a time!'}
    return render(request, 'machine_learning/intro.html',context=means)

def about(request):
    about_ml={'what':'Machine Learning is a subset of Artificial Intelligence that focuses on the development of computer programs that can access data and use it to learn for themselves.'}
    return render(request, 'machine_learning/about.html',context=about_ml)