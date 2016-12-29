from django.db import models

# Create your models here.

class Question(models.Model):

    question_description = models.CharField('Описание вопроса', max_length=50)
    question_text = models.TextField('Формулировка вопроса')

    def __str__(self):
        return ('%s' % self.question_description)


class Asset(models.Model):

    asset_question = models.ManyToManyField(Question)
    asset_result = models.CharField('Результат тестирования', max_length=50)
    asset_text_result = models.TextField('Подробный результат тестирования')


