"""readnow URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import demo.views as demo_views
import userprofile.views as userprofile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', demo_views.home, name='home'),
    path('books/', demo_views.books, name='books'),
    path('userprofile/',userprofile_views.userProfile, name='userprofile'),
    path('login/', demo_views.login, name='login'),
    path('registration/', demo_views.registration, name='registration'),



]
