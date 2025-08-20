"""
URL configuration for my_django_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from myapp.views import main_page, my_feed, login, logout, create, register, profile, set_password

urlpatterns = [
    path('', main_page, name='main_page'),
    path('', include('myapp.urls.article_urls'), name='article'),
    path('topics/',include('myapp.urls.topics_urls')),
    path('my_feed/',my_feed ,name='my_feed'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create/', create, name='create'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('set_password/', set_password, name='set_password'), 
]
