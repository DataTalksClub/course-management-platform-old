from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #...
    path('home/', TemplateView.as_view(template_name="users/login.html"), name='home'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
]