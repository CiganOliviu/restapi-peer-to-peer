from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from Stats.tests.test_dependencies import StatisticsBusinessPaths


class StatisticsStatusResponseTest(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.statistics_paths = StatisticsBusinessPaths()

    def test_stats_client_response(self):
        response = self.client.get(self.statistics_paths.build_client_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_teacher_response(self):
        response = self.client.get(self.statistics_paths.build_teacher_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_staff_response(self):
        response = self.client.get(self.statistics_paths.build_staff_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_expense_response(self):
        response = self.client.get(self.statistics_paths.build_expense_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_income_response(self):
        response = self.client.get(self.statistics_paths.build_income_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_feedback_response(self):
        response = self.client.get(self.statistics_paths.build_feedback_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_teacher_goal_response(self):
        response = self.client.get(self.statistics_paths.build_teacher_goal_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stats_student_expectations_response(self):
        response = self.client.get(self.statistics_paths.build_student_expectations_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
