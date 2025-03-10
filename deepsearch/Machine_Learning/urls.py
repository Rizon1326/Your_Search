
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/',views.machine_learning,name='ml_intro'),
    path('about/',views.about, name='ml_about'),
]
