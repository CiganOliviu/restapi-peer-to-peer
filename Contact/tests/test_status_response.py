from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from Contact.tests.tests_dependencies import ContactPaths


class ContactStatusResponseTest(APITestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.contact_paths = ContactPaths()

    def test_contact_response(self):
        response = self.client.get(self.contact_paths.build_contact_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
