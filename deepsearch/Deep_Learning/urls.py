
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/',views.deep_learning),
    path('about/',views.about),
   
]
