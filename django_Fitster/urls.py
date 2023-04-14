"""django_Fitster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the included() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('workouts/', views.workouts, name='workouts'),
    path('abs100/', views.abs100, name='abs100'),
    path('general', views.general, name='general'),
    path('marathon/', views.marathon, name='marathon'),
    path('running/', views.running, name='running'),
    path('totalburn/', views.total_burn, name='totalburn'),
    path('fitness/', views.fitness, name='fitness'),
    path('signup/', views.signup, name='signup'),
    path('insert', views.insertData, name='insertData'),
    path('list/', views.User_list, name='list')
]
