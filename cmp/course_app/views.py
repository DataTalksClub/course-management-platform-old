from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Homework


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
    context = {'homework': homework}
    return render(request, 'course_app/homework.html', context)

def submitHomework(request):
    context = {}
    return render(request, 'course_app/hw_form.html', context)


