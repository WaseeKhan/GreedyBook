from django.shortcuts import render
from .models import Profile
# Create your views here.
# ProfilesApp Views
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)

    context ={
        'profile':profile,
    }

    return render(request, 'profilesApp/myprofile.html',context)


