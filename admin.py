from django.contrib import admin

from .models import Question

admin.site.register(Question)

from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_tetxt"]

from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"field": ["question_text"]})
        ("Date information", {"fields": ["pub_date"]})
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

    admin.site.register(Question, QuestionAdmin)

from django.contrib import admin

from .models import Choice,Question

  #admin.site.register(Choice)

  from django.contrib import admin

  from .models import Choice,Question

  class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

  class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
        
    ]
    ]

# Register your models here.
