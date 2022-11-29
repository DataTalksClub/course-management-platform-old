from email.utils import format_datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Course, Homework, Submission
from .forms import QuestionForm


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course_app/courses.html', context)

def course(request, pk):
    courseObj = Course.objects.get(id=pk)
    # print('course ====>', courseObj)
    return render(request, 'course_app/course.html', {'course':courseObj})

def homework(request, pk):
    homework = Homework.objects.get(id=pk)
    post_data = request.POST if request.method == "POST" else None
    print("REQUEST====>", request.POST)
    print("HOMEWORK===>", homework.id)
    print("USER", request.user.id)
    submissions = Submission.objects.filter(user__email=request.user, homework__id=homework.id)
    
    if len(submissions) == 0:
        form = QuestionForm(homework, post_data, user=request.user )
    else:
        form = QuestionForm(homework, post_data, user=request.user,
            answer=submissions[0].answer)

    url = reverse("homework", args=(pk,))
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.')
        return redirect(url)
    context = {'homework': homework, 'form':form}
    # print('REQUEST', request.user)
    return render(request, 'course_app/homework.html', context)

# def submitHomework(request):
#     context = {}
#     return render(request, 'course_app/hw_form.html', context)


