from django.db import models


# Create your models here.

class Question_Manager(models.Manager):
    def create_question(self, question_description, question_text):
        question = self.create(question_description=question_description, question_text=question_text)
        return question


class Question(models.Model):
    question_description = models.CharField('Описание вопроса', max_length=50)
    question_text = models.TextField('Формулировка вопроса')

    objects = Question_Manager()

    def __str__(self):
        return ('%s' % self.question_description)

        # def __init__(self, question_description, question_text):
        #     self.question_text = question_text
        #     self.question_description = question_descriptionОписание испытания


class Assay_Manager(models.Manager):
    def create_assay(self, assay_description, assay_questions):
        assay = self.create(assay_description=assay_description)
        assay.save()
        for assay_question in assay_questions.all():
            assay.assay_question.add(assay_question)
        return assay


class Assay(models.Model):
    assay_question = models.ManyToManyField(Question)
    assay_description = models.CharField('123', max_length=50)
    assay_result = models.CharField('Результат тестирования', max_length=50)
    assay_text_result = models.TextField('Подробный результат тестирования')

    objects = Assay_Manager()

    def __str__(self):
        return ('%s' % self.assay_description)
