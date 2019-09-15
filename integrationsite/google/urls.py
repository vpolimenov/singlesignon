from django.urls import include, path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('logout', views.logout, name='logout'),
]
