from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from MathematicsDepartment.tests.test_dependencies import MathematicsDepartmentPaths


class MathematicsDepartmentStatusResponseTest(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.mathematics_department_paths = MathematicsDepartmentPaths()

    def test_mathematics_group_response(self):
        response = self.client.get(self.mathematics_department_paths.build_group_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mathematics_schedule_response(self):
        response = self.client.get(self.mathematics_department_paths.build_schedule_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mathematics_homework_response(self):
        response = self.client.get(self.mathematics_department_paths.build_homework_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
