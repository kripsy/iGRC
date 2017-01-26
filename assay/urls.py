from django.conf.urls import url, include
from assay.views import questions, question, edit_question, \
    delete_question, create_question, assays, edit_assay, assay, \
    delete_assay, create_assay, menu, add_question_text_input, delete_question_text_input, \
    add_question_number_input, delete_question_number_input, \
    add_question_text_area, delete_question_text_area

urlpatterns = [

    ######################################################################### questions
    url(r'^questions/(?P<question_id>[0-9]+)$', question, name='question'),
    url(r'^questions/(?P<question_id>[0-9]+)/edit_question$', edit_question, name='edit_question'),
    url(r'^questions/(?P<question_id>[0-9]+)/delete_question$', delete_question, name='delete_question'),
    url(r'^questions/create_question$', create_question, name='create_question'),
    url(r'^questions$', questions, name='questions'),

    #########################################################################  text input
    url(r'^questions/(?P<question_id>[0-9]+)/edit_question/add_question_text_input$', add_question_text_input,
        name='add_question_text_input'),
    url(r'^questions/delete_question_text_input$', delete_question_text_input,
        name='delete_question_text_input'),

    ######################################################################### number input
    url(r'^questions/(?P<question_id>[0-9]+)/edit_question/add_question_number_input$', add_question_number_input,
        name='add_question_number_input'),
    url(r'^questions/delete_question_number_input$', delete_question_number_input,
        name='delete_question_number_input'),

    #########################################################################  text area
    url(r'^questions/(?P<question_id>[0-9]+)/edit_question/add_question_text_area$', add_question_text_area,
        name='add_question_text_area'),
    url(r'^questions/delete_question_text_area$', delete_question_text_area,
        name='delete_question_text_area'),

    ######################################################################### assays
    url(r'^assays/(?P<assay_id>[0-9]+)$', assay, name='assay'),
    url(r'^assays/(?P<assay_id>[0-9]+)/edit_assay$', edit_assay, name='edit_assay'),
    url(r'^assays/(?P<assay_id>[0-9]+)/delete_assay$', delete_assay, name='delete_assay'),
    url(r'^assays/create_assay$', create_assay, name='create_assay'),
    url(r'^assays$', assays, name='assays'),

    ######################################################################### menu
    url(r'^menu$', menu, name='menu'),

]
