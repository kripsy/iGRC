from django import forms
from assay.models import Question


class Question_Edit(forms.Form):
    question_description = forms.CharField(label='Описание вопроса', max_length=50)
    question_text = forms.CharField(label='Формулировка вопроса', widget=forms.Textarea)


class Assay_Edit(forms.Form):
    # assay_question = forms.ModelForm.ManyToManyField('Список вопросов', Question)
    assay_question = forms.ModelMultipleChoiceField(queryset=Question.objects.all())
    assay_description = forms.CharField(label='Описание испытания', max_length=50)


# assay_result = forms.CharField('Результат тестирования', max_length=50)
#    assay_text_result = forms.CharField('Подробный результат тестирования', widget=forms.Textarea)

class Assay_View(forms.Form):
    assay_description = forms.CharField(label='Описание испытания', max_length=50,
                                        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
