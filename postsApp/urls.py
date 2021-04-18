from django.urls import path
from .views import post_comment_create_list_view

app_name = 'postsApp'

urlpatterns = [
    path('', post_comment_create_list_view,name='main-post-view'),
]