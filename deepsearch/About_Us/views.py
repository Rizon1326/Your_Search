from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    about={'what':'Our solution is designed to tackle complex challenges in industries ranging from healthcare to finance'}
    return render(request, 'about_us/about.html',context=about)