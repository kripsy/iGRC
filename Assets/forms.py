from django import forms


class Question_Edit(forms.Form):
    question_description = forms.CharField(label = 'Описание вопроса', max_length=50)
    question_text = forms.CharField(label = 'Формулировка вопроса', widget=forms.Textarea)

