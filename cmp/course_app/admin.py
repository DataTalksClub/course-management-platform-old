from django.contrib import admin

# Register your models here.
from .models import *

class HomeworkInLine(admin.TabularInline):
    model = Homework

class QuestionInLine(admin.TabularInline):
    model = Question
    
class HomeworkAdmin(admin.ModelAdmin):
    inlines = [ QuestionInLine ]

class QuestionAdmin(admin.ModelAdmin):
    fields = [ 'question', 'options', 'correct_answer', 'type' ]
    # some kind of a function that will add the title of homework and a number of a question

class CourseAdmin(admin.ModelAdmin):
    inlines = [ HomeworkInLine ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Leaderboard)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
admin.site.register(Enrolment)