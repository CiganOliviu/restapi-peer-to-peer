from rest_framework.test import APITestCase
from rest_framework.utils import json

from Contact.models import Contact
from Contact.tests.tests_dependencies import ContactPaths


class ContactDataResponseTest(APITestCase):

    def setUp(self):
        self.contact_paths = ContactPaths()
        Contact.objects.create(
            first_name='Ex1',
            last_name='Ex2',
            email='ex@ex.ex',
            client_type='teacher',
            subject='About teaching',
            phone_number='0723467123',
            message='ex message',
        )

        self.expected_json_response = {
            'id': 1,
            'first_name': 'Ex1',
            'last_name': 'Ex2',
            'email': 'ex@ex.ex',
            'client_type': 'teacher',
            'subject': 'About teaching',
            'phone_number': '0723467123',
            'message': 'ex message',
            'date': '',
        }

    def test_contact_response_data(self):
        response = self.client.get(self.contact_paths.build_contact_url(), format='json',
                                   content_type='application/json')

        self.expected_json_response['date'] = response.data[0]['date']

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)
