from django.shortcuts import render
from django.contrib.sites.models import Site


# Create your views here.
# Site.objects.get(name='back').id
def profile_view(request):
    # if request.user.is_authenticated():
    user = request.user
    print('user from profile_view', user.id)
    return render(request, 'account/profile.html')
