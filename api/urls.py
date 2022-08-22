from django.urls import path, include
from django.contrib.auth.models import User
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("auth/",obtain_auth_token),
    path("list/",ListCreateAPIView.as_view()),
    path("<int:pk>/update",updateAPIView.as_view()),
    path("<int:pk>/delete",deleteAPIView.as_view()),
    path('<int:pk>',detailAPIView.as_view()),
    path("answer/<str:slug>",AnsCreateListAPIView.as_view()),
    path("answer/<str:slug>/<int:pk>/update",AnsupdateAPIView.as_view()),
    path("answer/<str:slug>/<int:pk>/delete",AnsdeleteAPIView.as_view()),
    path("comment/<int:pk>",ComCreateListAPIView.as_view()),
    path("comment/<int:pk>/update",ComupdateAPIView.as_view()),
    path("comment/<int:pk>/delete",ComdeleteAPIView.as_view()),
]