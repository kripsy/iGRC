from django.db import models

# Create your models here.

class Question_Manager(models.Manager):
    def create_question(self, question_description, question_text):
        question = self.create(question_description = question_description, question_text = question_text)
        return question

class Question(models.Model):
    question_description = models.CharField('Описание вопроса', max_length=50)
    question_text = models.TextField('Формулировка вопроса')
    objects = Question_Manager()

    def __str__(self):
        return ('%s' % self.question_description)

    # def __init__(self, question_description, question_text):
    #     self.question_text = question_text
    #     self.question_description = question_description



class Asset(models.Model):

    asset_question = models.ManyToManyField(Question)
    asset_result = models.CharField('Результат тестирования', max_length=50)
    asset_text_result = models.TextField('Подробный результат тестирования')


