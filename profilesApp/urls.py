
from django.urls import path
from .views import ProfileDetailView, acceptInvitations, rejectInvitations, remove_from_friends, send_invitation,my_profile_view, invites_received_view,profiles_list_view, invite_profiles_list_view, ProfilelistView

app_name = 'profilesApp'

urlpatterns = [
    path('', ProfilelistView.as_view(), name='all-profiles-view'),
    path('myprofile/' ,my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invites/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', acceptInvitations, name='accept-invite'),
    path('my-invites/reject/', rejectInvitations, name='reject-invite'),
]
