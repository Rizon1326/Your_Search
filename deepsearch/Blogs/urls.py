
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blog/',views.blog1,name='blog'),
    path('forms/',views.showformsdata),
]
