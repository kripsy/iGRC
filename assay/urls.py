from django.conf.urls import url, include
from assay.views import questions, question, edit_question, delete_question, create_question, assays, edit_assay, assay, \
    delete_assay, create_assay, menu

urlpatterns = [
    url(r'^/questions/(?P<question_id>[0-9]+)$', question, name='question'),
    url(r'^/questions/(?P<question_id>[0-9]+)/edit_question$', edit_question, name='edit_question'),
    url(r'^/questions/(?P<question_id>[0-9]+)/delete_question$', delete_question, name='delete_question'),
    url(r'^/questions/create_question$', create_question, name='create_question'),
    url(r'^/questions$', questions, name='questions'),

    url(r'^/assays/(?P<assay_id>[0-9]+)$', assay, name='assay'),
    url(r'^/assays/(?P<assay_id>[0-9]+)/edit_assay$', edit_assay, name='edit_assay'),
    url(r'^/assays/(?P<assay_id>[0-9]+)/delete_assay$', delete_assay, name='delete_assay'),
    url(r'^/assays/create_assay$', create_assay, name='create_assay'),
    url(r'^/assays$', assays, name='assays'),

url(r'^/menu$', menu, name='menu'),

]
