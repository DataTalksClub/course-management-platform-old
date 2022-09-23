from email.utils import format_datetime
from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Homework
from .forms import QuestionForm


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course_app/courses.html', context)

def course(request, pk):
    courseObj = Course.objects.get(id=pk)
    print('course ====>', courseObj)
    return render(request, 'course_app/course.html', {'course':courseObj})

def homework(request, pk):
    homework = Homework.objects.get(id=pk)
    form = QuestionForm(homework)
    context = {'homework': homework, 'form':form}
    return render(request, 'course_app/homework.html', context)

# def submitHomework(request):
#     context = {}
#     return render(request, 'course_app/hw_form.html', context)


