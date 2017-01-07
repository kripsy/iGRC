from django.conf.urls import url, include
from django.contrib import admin
from mainmenu.views import menu


urlpatterns = [
    url(r'^', menu, name = 'menu'),
#    url(r'^logout/', logout, name='logout'),
]