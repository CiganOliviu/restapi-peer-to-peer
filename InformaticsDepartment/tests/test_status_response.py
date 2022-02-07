from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from InformaticsDepartment.tests.test_dependencies import InformaticsDepartmentPaths


class InformaticsDepartmentStatusResponseTest(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.informatics_department_paths = InformaticsDepartmentPaths()

    def test_informatics_group_response(self):
        response = self.client.get(self.informatics_department_paths.build_group_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_informatics_schedule_response(self):
        response = self.client.get(self.informatics_department_paths.build_schedule_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_informatics_homework_response(self):
        response = self.client.get(self.informatics_department_paths.build_homework_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
