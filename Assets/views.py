from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.http.response import Http404
from Assets.models import Question
from django.template.context_processors import csrf
from Assets.forms import Question_Edit


# Create your views here.

def questions(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['permission'] = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Questions"
    if ("Assets.delete_question" in args['permission']):
        args['assets_permission'] = True
        args['questions'] = Question.objects.all()
        return render_to_response('questions.html', args)
    else:
        return redirect("/")


def question(request, question_id=1):
    args = {}
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Question %s" % Question.objects.get(id=question_id).question_description
    question = Question.objects.get(id=question_id)
    if ("Assets.change_question" in user_permission):
        form_edit = Question_Edit(
            {'question_description': question.question_description, 'question_text': question.question_text})
        args['form_edit'] = form_edit
        return render_to_response('question.html', args)
    else:
        return redirect("/")


def edit_question(request, question_id=1):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Question %s" % Question.objects.get(id=question_id).question_description
    question = Question.objects.get(id=question_id)
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    question = Question.objects.get(id=question_id)
    form_edit = Question_Edit(request.POST)
    if ("Assets.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST and form_edit.is_valid():
            question.question_text = form_edit.cleaned_data['question_text']
            question.question_description = form_edit.cleaned_data['question_description']
            question.save()
            return redirect("/questions/%s" % question_id)
        else:
            form = Question_Edit(
                {'question_description': question.question_description, 'question_text': question.question_text})
            args['form_edit'] = form
            args['question_id'] = question_id
            return render_to_response('edit_question.html', args)
    else:
        return redirect("/questions")


def delete_question(request, question_id):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Удаление Question %s" % Question.objects.get(id=question_id).question_description
    question = Question.objects.get(id=question_id)
    user_permission = auth.get_user(request).get_group_permissions()
    question = Question.objects.get(id=question_id)
    if ("Assets.change_question" in auth.get_user(request).get_group_permissions()):
        question.delete()
    return redirect("/questions")


def create_question(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Создание Question"
    user_permission = auth.get_user(request).get_group_permissions()
    if ("Assets.change_question" in auth.get_user(request).get_group_permissions() and request.POST):
        question = Question_Edit(request.POST)
        if question.is_valid():
            new_question = Question.objects.create_question(question.cleaned_data['question_description'],
                                                            question.cleaned_data['question_text'])
            return redirect("/questions/%s" % new_question.id)
    args['form_edit'] = Question_Edit()
    return render_to_response('create_question.html', args)
