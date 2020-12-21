from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

from oauth2_provider.settings import oauth2_settings
from oauth2_provider.models import get_access_token_model,get_application_model
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

Application = get_application_model()
AccessToken = get_access_token_model()
UserModel = get_user_model()


class UserAuthTest(APITestCase):

    def setUp(self):

        oauth2_settings._SCOPES = ["read", "write"]

        self.test_user = UserModel.objects.create_user("ar2r4ik", "test2@example.com", "1234568")

        self.application = Application.objects.create(
                                                name="Test Application",
                                                redirect_uris="http://localhost http://example.com http://example.org",
                                                user=self.test_user,
                                                client_type=Application.CLIENT_CONFIDENTIAL,
                                                authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
                                            )

        self.access_token = AccessToken.objects.create(
                                                    user=self.test_user,
                                                    scope="read write",
                                                    expires=timezone.now() + timezone.timedelta(seconds=300),
                                                    token="secret-access-token-key",
                                                    application=self.application
                                                )
        # read or write as per your choice
        self.access_token.scope = "read"
        self.access_token.save()

        # correct token and correct scope
        self.auth =  "Bearer {0}".format(self.access_token.token)

    def test_success_response(self):

        url = reverse('login',)

        # Obtaining the POST response for the input data
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth)

        # checking wether the response is success