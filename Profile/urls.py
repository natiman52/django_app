from django.urls import path
from .views import Follow
from .EDViews import ProfileEdit

app_name = 'Profile'

urlpatterns = [
    path('Follow/',Follow, name='Follow' ),

]
