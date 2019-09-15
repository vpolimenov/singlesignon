import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from google import models
from django.conf import settings
from django.urls import reverse

from django.contrib.auth import logout as auth_logout

def index(request):
    template = loader.get_template('google/index.html')
    if request.user.is_authenticated:
        context = {
            'logged_in': request.user.is_authenticated,
            'username': f'{request.user.first_name} {request.user.last_name}',
            'can_disconnect': True
        }
    else:
        context = {
            'logged_in': request.user.is_authenticated,
        }
    return HttpResponse(template.render(context, request))


def logout(request):
    template = loader.get_template('google/index.html')
    auth_logout(request)
    context = {
        'logged_in': request.user.is_authenticated,
    }
    return HttpResponse(template.render(context, request))

