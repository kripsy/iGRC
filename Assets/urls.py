from django.conf.urls import url, include
from Assets.views import main

urlpatterns = [
    url(r'^', main, name = 'main'),

]
