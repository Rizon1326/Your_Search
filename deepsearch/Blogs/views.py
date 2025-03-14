from django.shortcuts import render
from django.http import HttpResponse
from . forms import TeachersRegistration

# Create your views here.
def blog1(request):
    status='Data Scientist'
    prerequisite='you have to enthusiast on ML'
    skills='Python,Stat and algorithms'
    focuses='To make LLM based product'
    blogs={'p':prerequisite,'s':skills,'f':focuses,'st':status}
    return render(request, 'blogs/blog.html',context=blogs)



def showformsdata(request):
    if request.method == 'POST':
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():
            print('Form is valid')
        else:
            print('Form is invalid')
    else:
        fm = TeachersRegistration()  # Initialize `fm` for GET requests

    return render(request, 'blogs/forms.html', {'form': fm})