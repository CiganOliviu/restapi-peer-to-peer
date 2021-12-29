from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from Details.tests.tests_dependencies import DetailsPaths


class DetailsStatusResponseTest(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.details_paths = DetailsPaths()

    def test_domain_response(self):
        response = self.client.get(self.details_paths.build_domain_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_high_school_profile_response(self):
        response = self.client.get(self.details_paths.build_high_school_profile_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_high_school_response(self):
        response = self.client.get(self.details_paths.build_high_school_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_town_response(self):
        response = self.client.get(self.details_paths.build_town_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_university_response(self):
        response = self.client.get(self.details_paths.build_university_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_faculty_response(self):
        response = self.client.get(self.details_paths.build_faculty_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_position_response(self):
        response = self.client.get(self.details_paths.build_position_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)