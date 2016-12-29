from django.contrib import admin
from Assets.models import Question, Asset

# Register your models here.

class Question_in_line(admin.StackedInline):
    model = Question
    extra = 5

class Asset_Admin(admin.ModelAdmin):
    fields = ['asset_question']



admin.site.register(Question)
admin.site.register(Asset, Asset_Admin)