from django.urls import path
from .Views.GET import UserGetRequests
from .Views.POST import UserPostRequests
from .Views.GET import ReviewGetRequests
from .Views.POST import ReviewPostRequests
from .Views.PUT import UserPutRequests
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserGetRequests.show_all, name='users'),
    path('users/<int:pk>/', UserGetRequests.view_user, name='user'),
    path('users/self/', UserGetRequests.view_own_user, name='view_own_profile'),
    path('users/banuser', UserPostRequests.ban_user, name='ban_user'),
    path('users/unbanuser', UserPostRequests.unban_user, name='unban_user'),
    path('register/', UserPostRequests.register_user, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('reviews/create/', ReviewPostRequests.register_review,name='register_review'),
    path('reviews/create/', ReviewPostRequests.register_review, name='register_review'),
    path('reviews/has_user_upvoted/<slug:review_id>', ReviewGetRequests.has_user_upvoted, name='has_user_upvoted'),
    path('reviews/has_user_downvoted/<slug:review_id>', ReviewGetRequests.has_user_downvoted, name='has_user_downvoted'),
    path('reviews/get_upvotes/<slug:review_id>', ReviewGetRequests.get_upvotes, name="get_upvotes"),
    path('reviews/get_downvotes/<slug:review_id>', ReviewGetRequests.get_downvotes, name="get_downvotes"),
    path('reviews/upvote/', ReviewPostRequests.upvote_review, name='upvote_review'),
    path('reviews/downvote/', ReviewPostRequests.downvote_review,name='downvote_review'),
    path('reviews/delete/', ReviewPostRequests.delete_review, name='delete_review'),
    path('reviews/', ReviewGetRequests.show_all, name='reviews'),
    path('users/update/username/', UserPutRequests.update_username, name='update_username'),
    path('users/update/firstname/', UserPutRequests.update_first_name, name='update_firstname'),
    path('users/update/lastname/', UserPutRequests.update_last_name, name='update_lastname'),
    path('users/update/email/', UserPutRequests.update_email, name='update_email'),
    

]
