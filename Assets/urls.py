from django.conf.urls import url, include
from Assets.views import questions, question, edit_question, delete_question, create_question

urlpatterns = [
    url(r'^/(?P<question_id>[0-9]+)$', question, name='question'),
    url(r'^/(?P<question_id>[0-9]+)/edit_question$', edit_question, name='edit_question'),
    url(r'^/(?P<question_id>[0-9]+)/delete_question$', delete_question, name='delete_question'),
    url(r'^/create_question$', create_question, name='create_question'),

    url(r'^$', questions, name='questions'),
]
