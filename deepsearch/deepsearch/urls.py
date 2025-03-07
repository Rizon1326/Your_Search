
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/',include('Machine_Learning.urls')),
    path('dl/',include('Deep_Learning.urls')),
    path('bl/',include('Blogs.urls')),
    path('about/',include('About_Us.urls')),
    path('da/',include('Data_Analysis.urls')),
]
