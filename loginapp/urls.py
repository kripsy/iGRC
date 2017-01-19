from django.conf.urls import url, include
from django.contrib import admin
from loginapp.views import login, logout


urlpatterns = [
    url(r'^login', login, name = 'login'),
    url(r'^logout', logout, name='logout'),
]