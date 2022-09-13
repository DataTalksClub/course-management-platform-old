from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses , name='courses'),
    path('course/<str:pk>', views.course, name='course'),
    path('homework/<str:pk>', views.homework, name='homework'),
    path('submit-homework/', views.submitHomework, name='submit-homework')
]