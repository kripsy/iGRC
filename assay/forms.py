from django import forms
from assay.models import Question_Text_Input, Question, Question_Number_Input


# необходимо учесть, что помимо полей вопроса должны быть поля ответов! Нужно это каким либо образом помечать!!!



######################################################################### Question


class Question_Edit(forms.Form):
    question_description = forms.CharField(label='Описание вопроса', max_length=50)
    question_text = forms.CharField(label='Формулировка вопроса', widget=forms.Textarea)


class Question_View(forms.Form):
    question_description = forms.CharField(label='Описание вопроса', max_length=50,
                                           widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_text = forms.CharField(label='Формулировка вопроса', widget=forms.Textarea(attrs={'readonly': 'readonly'}))



######################################################################### Assays
class Assay_Edit(forms.Form):
    assay_question = forms.ModelMultipleChoiceField(queryset=Question.objects.all())
    assay_description = forms.CharField(label='Описание испытания', max_length=50)


class Assay_View(forms.Form):
    assay_description = forms.CharField(label='Описание испытания', max_length=50,
                                        widget=forms.TextInput(attrs={'readonly': 'readonly'}))



######################################################################### question text input
class Question_Text_Input_Create(forms.Form):
    question_text_input_label = forms.CharField(label='Описание Question_Text_Input', max_length=50)
    question_text_input_value = forms.CharField(label='Значение Question_Text_Input', max_length=50)


class Question_Text_Input_View(Question_Text_Input_Create):
    question_text_input_label = forms.CharField(label='Описание Question_Text_Input', max_length=50,
                                                widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_text_input_value = forms.CharField(label='Значение Question_Text_Input', max_length=50,
                                                widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_text_input_id = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': 'readonly'}))

######################################################################### question number input
class Question_Number_Input_Create(forms.Form):
    question_number_input_label = forms.CharField(label='Описание Question_Number_Input', max_length=50)
    question_number_input_value = forms.IntegerField(label='Значение Question_Number_Input')


class Question_Number_Input_View(Question_Number_Input_Create):
    question_number_input_label = forms.CharField(label='Описание Question_Number_Input', max_length=50,
                                                  widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_number_input_value = forms.IntegerField(label='Значение Question_Number_Input',
                                                     widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_number_input_id = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': 'readonly'}))


######################################################################### question text area

class Question_Text_Area_Create(forms.Form):
    question_text_area_label = forms.CharField(label='Описание Question_Text_Area', max_length=50)
    question_text_area_value = forms.CharField(label='Значение Question_Text_Area', widget=forms.Textarea)


class Question_Text_Area_View(Question_Text_Area_Create):
    question_text_area_label = forms.CharField(label='Описание Question_Text_Area', max_length=50, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    question_text_area_value = forms.CharField(label = 'Значение Question_Text_Area', widget=forms.Textarea(attrs={'readonly': 'readonly'}))
    question_text_area_id = forms.CharField(widget=forms.HiddenInput(attrs={'readonly': 'readonly'}))