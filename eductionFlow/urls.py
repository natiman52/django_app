"""eductionFlow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from Profile.views import (profile,show_profile,Follow)
from Profile.EDViews import ProfileEdit,EditPhoto,DeleteUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('Users.urls')),
    path('',include('Main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('profile/',profile ,name='profile'),
    path('show-profile/<str:username>/',show_profile,name='show_profile'),
    path('Follow/',Follow, name='Follow' ),
    path('update/',ProfileEdit, name='UpdateProfile'),
    path('updatephoto/',EditPhoto, name="UpdatePhoto"),
    path('DeleteUser/',DeleteUser,name="Destroy"),
    path("api/",include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
