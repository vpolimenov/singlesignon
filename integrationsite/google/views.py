import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from google import models
from django.conf import settings
from django.urls import reverse

from django.contrib.auth import logout as auth_logout

def index(request):
    location = None

    template = loader.get_template('google/index.html')
    if request.user.is_authenticated:
        social = request.user.social_auth.get(provider='google-oauth2')
        user_info = requests.get(
            f"https://people.googleapis.com/v1/people/me",
            params={
                'access_token': social.extra_data['access_token'],
                'personFields': 'birthdays,biographies,addresses'
            }
        ).json()

        if 'addresses' in user_info:
            for i in user_info['addresses']:
                location = i['formattedValue'] if i['formattedType']=='Home' else None

        dob = user_info['birthdays'][0]['date'] if 'birthdays' in user_info.keys() else None
        bio = user_info['biographies'][0]['value'] if 'biographies' in user_info.keys() else None

        context = {
            'logged_in': request.user.is_authenticated,
            'username': f'{request.user.first_name} {request.user.last_name}',
            'birth_date': dob,
            'biography': bio,
            'location': location,
            'can_disconnect': True
        }
        request.user.bio = bio
        request.user.location = location
        request.user.birth_date = dob
        request.user.save()
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

