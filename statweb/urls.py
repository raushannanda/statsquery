"""statweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from statweb import views
from vlog import views as vlogview
from solution import views as solutionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blog/',vlogview.Vlog, name='blog'),
    path('privacy/',views.privacy, name='privacy'),
    path('terms/',views.terms,name='terms'),
    path('blog/<int:slug>/',vlogview.Vloglink,name='activeblog'),
    path('posts/<str:postid>',vlogview.Posts,name='post'),
    path('solution',solutionView.Solution,name='solution'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
]
