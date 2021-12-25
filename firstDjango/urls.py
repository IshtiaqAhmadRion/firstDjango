
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import  HomePage,FirstPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",FirstPage),
    path("",HomePage),
   

    
]
