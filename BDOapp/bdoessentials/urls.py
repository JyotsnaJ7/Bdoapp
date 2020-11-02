"""BDOapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bdoessentials.views import createLead,register,leadDetails,leadEdit,landingpage,followupview,upcomingfollowupview,leadDelete

urlpatterns = [
    path('create',createLead,name='createlead'),
    path('',landingpage,name='landingpage'),
    path('register',register,name='register'),
    path('leaddetails<int:pk>',leadDetails,name='leaddetails'),
    path('leadedit<int:pk>',leadEdit,name='leadedit'),
    path('followupview<int:pk>',followupview,name='followupview'),
    path('upcomingfollowupview<int:pk>',upcomingfollowupview,name='upcomingfollowupview'),
    path('leaddelete<int:pk>',leadDelete,name='leaddelete'),

]
