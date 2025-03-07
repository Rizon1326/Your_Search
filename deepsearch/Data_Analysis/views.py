from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data_analysis(request):
    data_analysis={'what':'Turn data into knowledge, and knowledge into power!'}
    return render(request, 'data_analysis/data_analysis.html',context=data_analysis)