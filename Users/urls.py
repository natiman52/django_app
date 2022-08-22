from django.urls import path
from .views import SignUp,login,logout
app_name='users'
urlpatterns = [
    path('signup',SignUp,name='signup'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'), 
]