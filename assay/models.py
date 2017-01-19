from django.db import models


# Create your models here.


# template classes
# - обычный text_input
# - text_area
# - select_menus
# - multiple select menus
# - checkbox (множественный выбор)
# - radio buttons
#
class Question_Text_Input_Manager(models.Manager):
    def create_question_text_input(self, question_text_input_label, question_text_input_value):
        question_text_input = self.create(question_text_input_label=question_text_input_label,
                                          question_text_input_value=question_text_input_value)
        return question_text_input


class Assay_Manager(models.Manager):
    def create_assay(self, assay_description, assay_questions):
        assay = self.create(assay_description=assay_description)
        assay.save()
        for assay_question in assay_questions.all():
            assay.assay_question.add(assay_question)
        return assay


class Question_Manager(models.Manager):
    def create_question(self, question_description, question_text):
        question = self.create(question_description=question_description, question_text=question_text)
        return question


class Question_Text_Input(models.Model):
    question_text_input_label = models.CharField('Описание Question_Text_Input', max_length=50)
    question_text_input_value = models.CharField('Значение Question_Text_Input', max_length=50)
    question_text_input_question = models.ForeignKey('Question', null=True)
    objects = Question_Text_Input_Manager()

    def __str__(self):
        return ('%s' % self.question_text_input_label)


class Question_Text_Area(models.Model):
    question_text_area_label = models.CharField('Описание Question_Text_Area', max_length=50)
    question_text_input_value = models.TextField('Значение Question_Text_Area')


class Question_Number_Input(models.Model):
    question_number_input_label = models.CharField('Описание Question_Text_Input', max_length=50)
    question_number_input_value = models.IntegerField('Значение Question_Number_Input')

class Question(models.Model):
    question_description = models.CharField('Описание вопроса', max_length=50)
    question_text = models.TextField('Формулировка вопроса')

    objects = Question_Manager()

    def __str__(self):
        return ('%s' % self.question_description)


class Assay(models.Model):
    assay_question = models.ManyToManyField(Question)
    assay_description = models.CharField('123', max_length=50)
    assay_result = models.CharField('Результат тестирования', max_length=50)
    assay_text_result = models.TextField('Подробный результат тестирования')

    objects = Assay_Manager()

    def __str__(self):
        return ('%s' % self.assay_description)