from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses , name='courses'),
    path('course/<str:pk>', views.course, name='course')
]