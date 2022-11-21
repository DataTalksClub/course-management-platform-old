from django.urls import path, include
from django.views.generic import TemplateView
# from django.contrib.auth.views import
from .views import *

urlpatterns = [
    #...
    path('', TemplateView.as_view(template_name="users/login.html"), name='home'),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name='account_profile'),
]