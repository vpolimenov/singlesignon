from django.test import TestCase, Client
from google.models import User
import requests
from django.urls import reverse


class Login(TestCase):

    client = Client()

    def test_client_not_logged_in(self):
        assert self.client.get('').context['logged_in'] == False

    def test_client_logged_in(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        logged_in = self.client.login(username='testuser', password='12345')
        assert logged_in == True

    def test_social_oauth_old_token(self):
        dummy_access_code = 'ya29.GluEB1bXg3VVZ-VZvUyZ4FxuIwFAoGi988kWAh6drYcxeOZfcwhA0fEy80SJsMIPsWaXmu1nY0j-2bDdVO20ynn7CXVNI6NSFLhvnTRv_32KMkUJEtKwFehNkvWA'
        user_info = requests.get(
            f"https://people.googleapis.com/v1/people/me",
            params={
                'access_token': dummy_access_code,
                'personFields': 'birthdays,biographies,addresses'
            }
        ).json()
        assert user_info['error']['status'] == 'UNAUTHENTICATED'

    def test_social_oauth_working(self):
        raise NotImplementedError

