from django.urls import path
from django.conf.urls import include, url
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls', namespace='social')),
    path('logout', views.logout, name='logout'),
]
