
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('data_analysis/',views.data_analysis,name='data_analysis'),
   
]

