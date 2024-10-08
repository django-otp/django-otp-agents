from django_otp.tests import TestCase

from django.apps import apps
from django.db import IntegrityError
from django.test import override_settings


@override_settings(ROOT_URLCONF='otp_agents.test.urls')
class OTPAgentsTestCase(TestCase):
    def setUp(self):
        self._check_for_otp_static()

        try:
            self.alice = self.create_user('alice', 'alice')
        except IntegrityError:
            self.skipTest("Unable to create a test user")
        else:
            device = self.alice.staticdevice_set.create()
            device.token_set.create(token='alice1')
            device.token_set.create(token='alice2')

    def _check_for_otp_static(self):
        try:
            apps.get_app_config('otp_static')
        except LookupError:
            self.skipTest("Requires django_otp.plugins.otp_static")

    def test_otp_anonymous(self):
        response = self.client.get('/otp/')

        self.assertEqual(response.status_code, 302)

    def test_otp_authenticated(self):
        self.login()
        response = self.client.get('/otp/')

        self.assertEqual(response.status_code, 302)

    def test_otp_verified(self):
        self.verify()
        response = self.client.get('/otp/')

        self.assertEqual(response.status_code, 200)

    def test_otp_trusted(self):
        self.trust(True)
        self.logout()
        self.login()
        response = self.client.get('/otp/')

        self.assertEqual(response.status_code, 302)

    def test_otp2_verified(self):
        self.verify()
        response = self.client.get('/otp2/')

        self.assertEqual(response.status_code, 200)

    def test_otp_advised_anonymous(self):
        response = self.client.get('/otp_advised/')

        self.assertEqual(response.status_code, 302)

    def test_otp_advised_unconfigured(self):
        self.alice.staticdevice_set.all().delete()
        self.login()
        response = self.client.get('/otp_advised/')

        self.assertEqual(response.status_code, 200)

    def test_otp_advised_unconfigured_2(self):
        self.alice.staticdevice_set.all().delete()
        self.login()
        response = self.client.get('/otp_advised_2/')

        self.assertEqual(response.status_code, 200)

    def test_otp_advised_authenticated(self):
        self.login()
        response = self.client.get('/otp_advised/')

        self.assertEqual(response.status_code, 302)

    def test_otp_advised_verified(self):
        self.verify()
        response = self.client.get('/otp_advised/')

        self.assertEqual(response.status_code, 200)

    def test_agent_anonymous(self):
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 302)

    def test_agent_authenticated(self):
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 302)

    def test_agent_verified(self):
        self.verify()
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 200)

    def test_agent_trusted_session(self):
        self.trust(False)
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 200)

    def test_agent_trusted(self):
        self.trust(True)
        self.logout()
        self.login()
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 200)

    def test_two_step_trust(self):
        self.login()
        self.add_trust(True)
        self.logout()
        self.login()
        response = self.client.get('/agent/')

        self.assertEqual(response.status_code, 200)

    #
    # Helpers
    #

    def login(self):
        params = {
            'username': 'alice',
            'password': 'alice',
        }

        response = self.client.post('/login/', params)

        self.assertEqual(response.status_code, 302)

    def verify(self):
        params = {
            'username': 'alice',
            'password': 'alice',
            'otp_token': 'alice1',
        }

        response = self.client.post('/verify/', params)

        self.assertEqual(response.status_code, 302)

    def trust(self, persist=False):
        params = {
            'username': 'alice',
            'password': 'alice',
            'otp_token': 'alice1',
            'otp_trust_agent': '1' if persist else '',
        }

        response = self.client.post('/trust/', params)

        self.assertEqual(response.status_code, 302)

    def add_trust(self, persist=False):
        params = {
            'otp_device': 'otp_static.staticdevice/1',
            'otp_token': 'alice1',
            'otp_trust_agent': '1' if persist else '',
        }

        response = self.client.post('/trust/', params)

        self.assertEqual(response.status_code, 302)

    def logout(self):
        response = self.client.post('/logout/')

        self.assertEqual(response.status_code, 200)
