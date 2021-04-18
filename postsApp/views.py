from django.shortcuts import render,redirect
from .models import Post, Like
from profilesApp.models import Profile


# Create your views here.

def post_comment_create_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    context = {'qs': qs,'profile':profile, }

    return render(request, 'postsApp/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value = 'Like'
            post_obj.save()
            like.save()
    return redirect('postsApp:main-post-view')