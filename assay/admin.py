from django.contrib import admin
from assay.models import Question, Assay


# Register your models here.

class Question_in_line(admin.StackedInline):
    model = Question
    extra = 5


class Assay_Admin(admin.ModelAdmin):
    fields = ['assay_description', 'assay_result', 'assay_text_result', 'assay_question']


admin.site.register(Question)
admin.site.register(Assay, Assay_Admin)
