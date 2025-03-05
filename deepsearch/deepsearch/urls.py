"""
URL configuration for deepsearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Machine_Learning.views import machine_learning
from Machine_Learning.views import about
from Deep_Learning.views import deep_learning
from Deep_Learning.views import about
from Blogs.views import blog1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',machine_learning),
    path('about_ml/',about),
    path('deep_learning/',deep_learning),
    path('about_dl/',about),
    path('blog1/',blog1),
    
]
