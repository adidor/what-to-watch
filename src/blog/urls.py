from os import path
from .views import index, vpn
from django.urls import path

urlpatterns = [
    path('', index, name = "blog-index"),
    #path('vpn', vpn, name='second_page'),
]