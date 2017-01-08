from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponse
from django.http.response import Http404

# Create your views here.


def menu(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['permission'] = auth.get_user(request).get_group_permissions()
    args['action'] = "Главное меню"
    if ("Assets.delete_question" in args['permission']):
        args['assets_permission'] = True
    else:
        args['assets_permission'] = False
    return render_to_response('main.html', args)