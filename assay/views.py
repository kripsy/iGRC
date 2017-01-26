from django.contrib import auth
from django.shortcuts import render, render_to_response, \
    HttpResponse, redirect
from django.http.response import Http404
from assay.models import Question, Assay, \
    Question_Text_Input, Question_Number_Input, \
    Question_Text_Area
from django.template.context_processors import csrf
from assay.forms import Question_Edit, Question_View, \
    Assay_Edit, Assay_View, \
    Question_Text_Input_Create, Question_Text_Input_View, \
    Question_Number_Input_Create, Question_Number_Input_View, \
    Question_Text_Area_Create, Question_Text_Area_View


# Create your views here.

######################################################################### questions

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
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
    if ("assay.change_question" in user_permission):

        ########################## forms for question details
        form_question_text_input = []
        form_question_number_input = []
        form_question_text_area = []
        ##########################


        form_question = Question_View(
            {'question_description': question.question_description, 'question_text': question.question_text})

        ################################## insert into question forms for details
        if (Question_Text_Input.objects.filter(question_text_input_question_id=question_id)):
            for question_text_input in Question_Text_Input.objects.filter(question_text_input_question_id=question_id):
                form_temp = Question_Text_Input_View(
                    {'question_text_input_label': question_text_input.question_text_input_label,
                     'question_text_input_value': question_text_input.question_text_input_value,
                     'question_text_input_id': question_text_input.id})
                form_question_text_input.insert(len(form_question_text_input), form_temp)

        if (Question_Number_Input.objects.filter(question_number_input_question_id=question_id)):
            for question_number_input in Question_Number_Input.objects.filter(
                    question_number_input_question_id=question_id):
                form_temp = Question_Number_Input_View(
                    {'question_number_input_label': question_number_input.question_number_input_label,
                     'question_number_input_value': question_number_input.question_number_input_value,
                     'question_number_input_id': question_number_input.id})
                form_question_number_input.insert(len(form_question_number_input), form_temp)

        if (Question_Text_Area.objects.filter(question_text_area_question_id=question_id)):
            for question_text_area in Question_Text_Area.objects.filter(
                    question_text_area_question_id=question_id):
                form_temp = Question_Text_Area_View(
                    {'question_text_area_label': question_text_area.question_text_area_label,
                     'question_text_area_value': question_text_area.question_text_area_value,
                     'question_text_area_id': question_text_area.id})
                form_question_text_area.insert(len(form_question_text_area), form_temp)

        ######################## parameters
        args['form_question'] = form_question
        args['form_question_text_input'] = form_question_text_input
        args['form_question_number_input'] = form_question_number_input
        args['form_question_text_area'] = form_question_text_area

        return render_to_response('question.html', args)
    else:
        return redirect("/")


def edit_question(request, question_id=1):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Question %s" % Question.objects.get(id=question_id).question_description
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
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

            ########################## forms for question details
            form_question_text_input = []
            form_question_number_input = []
            form_question_text_area = []

            ######################################

            ################################## insert into question forms for details
            if (Question_Text_Input.objects.filter(question_text_input_question_id=question_id)):
                for question_text_input in Question_Text_Input.objects.filter(
                        question_text_input_question_id=question_id):
                    form_temp = Question_Text_Input_View(
                        {'question_text_input_label': question_text_input.question_text_input_label,
                         'question_text_input_value': question_text_input.question_text_input_value,
                         'question_text_input_id': question_text_input.id})
                    form_question_text_input.insert(len(form_question_text_input), form_temp)

            if (Question_Number_Input.objects.filter(question_number_input_question_id=question_id)):
                for question_number_input in Question_Number_Input.objects.filter(
                        question_number_input_question_id=question_id):
                    form_temp = Question_Number_Input_View(
                        {'question_number_input_label': question_number_input.question_number_input_label,
                         'question_number_input_value': question_number_input.question_number_input_value,
                         'question_number_input_id': question_number_input.id})
                    form_question_number_input.insert(len(form_question_number_input), form_temp)

            if (Question_Text_Area.objects.filter(question_text_area_question_id=question_id)):
                for question_text_area in Question_Text_Area.objects.filter(
                        question_text_area_question_id=question_id):
                    form_temp = Question_Text_Area_View(
                        {'question_text_area_label': question_text_area.question_text_area_label,
                         'question_text_area_value': question_text_area.question_text_area_value,
                         'question_text_area_id': question_text_area.id})
                    form_question_text_area.insert(len(form_question_text_area), form_temp)

            ######################## parameters
            args['form_question_text_input'] = form_question_text_input
            args['form_question_number_input'] = form_question_number_input
            args['form_question_text_area'] = form_question_text_area
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
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
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


######################################################################### assays

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
    try:
        assay = Assay.objects.get(id=assay_id)
    except Assay.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
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


def assay(request, assay_id):
    args = {}
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    args['action'] = "Просмотр Assay id = %s" % Assay.objects.get(id=assay_id).id
    try:
        assay = Assay.objects.get(id=assay_id)
    except Assay.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
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
    # args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Удаление Assay id =  %s" % Assay.objects.get(id=assay_id).id

    try:
        assay = Assay.objects.get(id=assay_id)
    except Assay.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

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


######################################################################### menu

def menu(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['action'] = "Меню Assay"
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        return render_to_response('assay_menu.html', args)
    return redirect('/')


######################################################################### question_text_input

def add_question_text_input(request, question_id):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Question %s добавление question_text_input" % question_id

    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST:
            form = Question_Text_Input_Create(request.POST)
            if form.is_valid():
                question_text_input = Question_Text_Input.objects.create_question_text_input(
                    form.cleaned_data['question_text_input_label'], form.cleaned_data['question_text_input_value'])
                question_text_input.save()
                question.question_text_input_set.add(question_text_input)
                question.save()
                return redirect("/assay/questions/%s/edit_question" % question_id)
        else:
            form = Question_Text_Input_Create()
            args['form'] = form
            args['question_id'] = question_id
            return render_to_response('assay_edit_question_add_question_text_input.html', args)
    else:
        return redirect("/assay/questions")


def delete_question_text_input(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if (request.POST):
        if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
            question_text_input_id = request.POST.get('question_text_input_id', '')
            try:
                question_text_input = Question_Text_Input.objects.get(id=question_text_input_id)
            except Question_Text_Input.DoesNotExist:
                return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

            question_text_input.delete()

    return redirect("%s" % request.META.get('HTTP_REFERER', '/'))


######################################################################### question_number_input

def add_question_number_input(request, question_id):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Question %s добавление question_text_input" % question_id

    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST:
            form = Question_Number_Input_Create(request.POST)
            if form.is_valid():
                question_number_input = Question_Number_Input.objects.create_question_number_input(
                    form.cleaned_data['question_number_input_label'], form.cleaned_data['question_number_input_value'])
                question_number_input.save()
                question.question_number_input_set.add(question_number_input)
                question.save()
                return redirect("/assay/questions/%s/edit_question" % question_id)
        else:
            form = Question_Number_Input_Create()
            args['form'] = form
            args['question_id'] = question_id
            return render_to_response('assay_edit_question_add_question_number_input.html', args)
    else:
        return redirect("/assay/questions")


def delete_question_number_input(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if (request.POST):
        if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
            question_number_input_id = request.POST.get('question_number_input_id', '')
            try:
                question_number_input = Question_Number_Input.objects.get(id=question_number_input_id)
            except Question_Number_Input.DoesNotExist:
                return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

            question_number_input.delete()

    return redirect("%s" % request.META.get('HTTP_REFERER', '/'))


######################################################################### question_text_area

def add_question_text_area(request, question_id):
    args = {}
    args.update(csrf(request))
    args['action'] = "Редактирование Question %s добавление question_text_area" % question_id

    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
        if request.POST:
            form = Question_Text_Area_Create(request.POST)
            if form.is_valid():
                question_text_area = Question_Text_Area.objects.create_text_area(
                    form.cleaned_data['question_text_area_label'], form.cleaned_data['question_text_area_value'])
                question_text_area.save()
                question.question_text_area_set.add(question_text_area)
                question.save()
                return redirect("/assay/questions/%s/edit_question" % question_id)
        else:
            form = Question_Text_Area_Create()
            args['form'] = form
            args['question_id'] = question_id
            return render_to_response('assay_edit_question_add_question_text_area.html', args)
    else:
        return redirect("/assay/questions")


def delete_question_text_area(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    user_permission = auth.get_user(request).get_group_permissions()
    if (request.POST):
        if ("assay.change_question" in auth.get_user(request).get_group_permissions()):
            question_text_area_id = request.POST.get('question_text_area_id', '')
            try:
                question_text_area = Question_Text_Area.objects.get(id=question_text_area_id)
            except Question_Text_Area.DoesNotExist:
                return redirect("%s" % request.META.get('HTTP_REFERER', '/'))

            question_text_area.delete()

    return redirect("%s" % request.META.get('HTTP_REFERER', '/'))
