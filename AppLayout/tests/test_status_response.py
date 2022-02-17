from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from AppLayout.tests.tests_dependencies import AppDependenciesPaths


class AppDependenciesStatusResponseTests(APITestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.constants = AppDependenciesPaths()

    def test_hero_card_response(self):
        response = self.client.get(self.constants.build_hero_card_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_homework_card_response(self):
        response = self.client.get(self.constants.build_homework_card_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schedule_card_response(self):
        response = self.client.get(self.constants.build_schedule_card_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_content_section_response(self):
        response = self.client.get(self.constants.build_content_section_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_content_image_section_response(self):
        response = self.client.get(self.constants.build_content_image_section_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_content_response(self):
        response = self.client.get(self.constants.build_home_content_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
