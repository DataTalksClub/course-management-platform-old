from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course_app/courses.html', context)

def course(request, pk):
    courseObj = Course.objects.get(id=pk)
    return render(request, 'course_app/course.html', {'course':courseObj})


