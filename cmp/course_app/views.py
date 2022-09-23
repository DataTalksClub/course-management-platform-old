from email.utils import format_datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

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
    post_data = request.POST if request.method == "POST" else None
    form = QuestionForm(homework, post_data)

    url = reverse("homework", args=(pk,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    context = {'homework': homework, 'form':form}
    return render(request, 'course_app/homework.html', context)

# def submitHomework(request):
#     context = {}
#     return render(request, 'course_app/hw_form.html', context)


