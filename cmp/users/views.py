from django.shortcuts import render
from django.contrib.sites.models import Site


# Create your views here.
# Site.objects.get(name='back').id
def profile_view(request):
    return render(request, 'account/profile.html')
