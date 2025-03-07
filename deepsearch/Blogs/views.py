from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog1(request):
    status='Data Scientist'
    prerequisite='you have to enthusiast on ML'
    skills='Python,Stat and algorithms'
    focuses='To make LLM based product'
    blogs={'p':prerequisite,'s':skills,'f':focuses,'st':status}
    return render(request, 'blogs/blog.html',context=blogs)