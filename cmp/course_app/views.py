from django.shortcuts import render
from django.http import HttpResponse

coursesList = [
    {
        'id':'1',
        'title':'Machine Learning Zoomcamp',
        'description':'Waht, never heard of it',
    },
    {
        'id':'2',
        'title':'Course n2',
        'description':'Waht, never heard of it',
    },
    {
        'id':'3',
        'title':'MLOPs',
        'description':'Waht, never heard of it',
    }
]

def courses(request):
    context = {'courses': coursesList}
    return render(request, 'course_app/courses.html', context)

def course(request, pk):
    courseObj = None
    for i in coursesList:
        if i['id'] == pk:
            courseObj = i

    return render(request, 'course_app/course.html', {'course':courseObj})


