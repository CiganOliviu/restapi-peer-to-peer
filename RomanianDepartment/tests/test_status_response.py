from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from RomanianDepartment.tests.test_dependencies import RomanianDepartmentPaths


class RomanianDepartmentStatusResponseTest(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.romanian_department_paths = RomanianDepartmentPaths()

    def test_romanian_group_response(self):
        response = self.client.get(self.romanian_department_paths.build_group_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_romanian_schedule_response(self):
        response = self.client.get(self.romanian_department_paths.build_schedule_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_romanian_homework_response(self):
        response = self.client.get(self.romanian_department_paths.build_homework_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
