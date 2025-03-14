from django.shortcuts import render
from django.http import HttpResponse
from About_Us.models import Teachers
# Create your views here.
def about(request):
    return render(request, 'about_us/about.html')


def teachers_info(request):
    teach=Teachers.objects.all()
    
    return render(request, 'about_us/teachers.html',{'teachers':teach})