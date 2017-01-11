from django.contrib import auth
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.http.response import Http404
from assay.models import Question, Assay
from django.template.context_processors import csrf
from assay.forms import Question_Edit, Assay_Edit, Assay_View


# Create your views here.

def questions(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['permission'] = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Questions"
    if ("assay.delete_question" in args['permission']):
        args['assay_permission'] = True
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
    if ("assay.change_question" in user_permission):
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
    form_edit = Question_Edit(request.POST)
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST and form_edit.is_valid():
            question.question_text = form_edit.cleaned_data['question_text']
            question.question_description = form_edit.cleaned_data['question_description']
            question.save()
            return redirect("/assay/questions/%s" % question_id)
        else:
            form = Question_Edit(
                {'question_description': question.question_description, 'question_text': question.question_text})
            args['form_edit'] = form
            args['question_id'] = question_id
            return render_to_response('edit_question.html', args)
    else:
        return redirect("/assay/questions")


def delete_question(request, question_id):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Удаление Question %s" % Question.objects.get(id=question_id).question_description
    question = Question.objects.get(id=question_id)
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        question.delete()
    return redirect("/assay/questions")


def create_question(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Создание Question"
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions() and request.POST):
        question = Question_Edit(request.POST)
        if question.is_valid():
            new_question = Question.objects.create_question(question.cleaned_data['question_description'],
                                                            question.cleaned_data['question_text'])
            return redirect("/assay/questions/%s" % new_question.id)
    args['form_edit'] = Question_Edit()
    return render_to_response('create_question.html', args)


def assays(request):
    args = {}
    args['username'] = auth.get_user(request).username
    args['permission'] = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Assays"
    if ("assay.delete_question" in args['permission']):
        args['assay_permission'] = True
        args['assays'] = Assay.objects.all()
        return render_to_response('assays.html', args)
    else:
        return redirect("/")


def edit_assay(request, assay_id=1):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Assay id = %s" % Assay.objects.get(id=assay_id).id
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    assay = Assay.objects.get(id=assay_id)
    form_edit = Assay_Edit(request.POST)
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST and form_edit.is_valid():
            assay.assay_question = form_edit.cleaned_data['assay_question']
            assay.assay_description = form_edit.cleaned_data['assay_description']
            assay.save()
            return redirect("/assay/assays/%s" % assay_id)
        else:
            form_edit = Assay_Edit(
                {'assay_description': assay.assay_description, 'assay_question': assay.assay_question.all()})
            args['form_edit'] = form_edit
            args['assay_id'] = assay_id
            return render_to_response('edit_assay.html', args)
    else:
        return redirect("/assay/assays")


def assay(request, assay_id=1):
    args = {}
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Assay id = %s" % Assay.objects.get(id=assay_id).id
    assay = Assay.objects.get(id=assay_id)
    if ("assay.change_question" in user_permission):
        form = Assay_View(
            {'assay_description': assay.assay_description})
        args['form'] = form
        args['assay'] = assay
        return render_to_response('assay.html', args)
    else:
        return redirect("/")


def delete_assay(request, assay_id):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Удаление Assay id =  %s" % Assay.objects.get(id=assay_id).id
    assay = Assay.objects.get(id=assay_id)
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        assay.delete()
    return redirect("/assay/assays")


def create_assay(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Создание Assay"
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions() and request.POST):
        assay = Assay_Edit(request.POST)
        if assay.is_valid():
            new_assay = Assay.objects.create_assay(assay.cleaned_data['assay_description'],
                                                   assay.cleaned_data['assay_question'])
            return redirect("/assay/assays/%s" % new_assay.id)
    args['form'] = Assay_Edit()
    return render_to_response('create_assay.html', args)


def menu(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Меню Assay"
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        return render_to_response('assay_menu.html', args)
    return redirect('/')