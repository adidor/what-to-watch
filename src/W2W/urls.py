"""W2W URL Configuration

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
from django.urls import include, path
from blog.views import genre_vpn, index, vpn, vpn_yes, vpn_no, genre

#from W2W import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='first_page'),
    #path('blog/', include("blog.urls")),
    path('vpn', vpn, name='second_page'),
    path('vpn_yes', vpn_yes, name='third_page_yes'),
    path('vpn_no', vpn_no, name='third_page_no'),
    path('genre', genre, name='genre'),
    path('genre_vpn', genre_vpn, name='genre_vpn'),




] #+ static()
