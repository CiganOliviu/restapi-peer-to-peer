from rest_framework.test import APITestCase
from rest_framework.utils import json

from Details.models import *
from Details.tests.tests_dependencies import DetailsPaths


class DomainDataResponseTest(APITestCase):

    def setUp(self):
        self.details_paths = DetailsPaths()
        Domain.objects.create(
            domain='Informatics'
        )

        self.expect_json_response = {
            'id': 1,
            'domain': 'Informatics',
        }

    def test_domain_response_data(self):
        response = self.client.get(self.details_paths.build_domain_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class HighSchoolProfileDataResponseTest(APITestCase):

    def setUp(self):
        self.details_paths = DetailsPaths()
        HighSchoolProfile.objects.create(
            profile='Matematica-Informatica'
        )

        self.expect_json_response = {
            'id': 1,
            'profile': 'Matematica-Informatica',
        }

    def test_high_school_profile_response_data(self):
        response = self.client.get(self.details_paths.build_high_school_profile_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class HighSchoolDataResponseTest(APITestCase):

    def setUp(self):
        self.details_paths = DetailsPaths()
        HighSchool.objects.create(
            name='Liceul Teoretic Carei'
        )

        self.expect_json_response = {
            'id': 1,
            'name': 'Liceul Teoretic Carei',
        }

    def test_high_school_response_data(self):
        response = self.client.get(self.details_paths.build_high_school_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class TownDataResponseTest(APITestCase):

    def setUp(self):
        self.details_paths = DetailsPaths()
        Town.objects.create(
            name='Cluj-Napoca'
        )

        self.expect_json_response = {
            'id': 1,
            'name': 'Cluj-Napoca',
        }

    def test_town_response_data(self):
        response = self.client.get(self.details_paths.build_town_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class UniversityDataResponseTest(APITestCase):

    def setUp(self):
        self.details_paths = DetailsPaths()

        Town.objects.create(
            name='Cluj-Napoca'
        )

        Universitie.objects.create(
            name='Tehnical University Of Cluj-Napoca',
            town=Town.objects.get(name='Cluj-Napoca')
        )

        self.expect_json_response = {
            'id': 1,
            'name': 'Tehnical University Of Cluj-Napoca',
            'town': {'id': 1, 'name': 'Cluj-Napoca'}
        }

    def test_university_response_data(self):
        response = self.client.get(self.details_paths.build_university_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class FacultyDataResponseTest(APITestCase):

    def setUp(self):
        self.details_path = DetailsPaths()

        Town.objects.create(
            name='Cluj-Napoca'
        )

        Universitie.objects.create(
            name='Tehnical University Of Cluj-Napoca',
            town=Town.objects.get(name='Cluj-Napoca')
        )

        Facultie.objects.create(
            university=Universitie.objects.get(name='Tehnical University Of Cluj-Napoca',
                                               town=Town.objects.get(name='Cluj-Napoca')),
            name='Tehnical University Of Cluj-Napoca'
        )

        self.expect_json_response = {
            'id': 1,
            'name': 'Tehnical University Of Cluj-Napoca',
            'university': {
                'id': 1,
                'name': 'Tehnical University Of Cluj-Napoca',
                'town': {
                    'id': 1,
                    'name': 'Cluj-Napoca'
                }
            }
        }

    def test_faculty_response_data(self):
        response = self.client.get(self.details_path.build_faculty_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class PositionDataResponseTest(APITestCase):

    def setUp(self):
        self.detail_paths = DetailsPaths()

        Position.objects.create(
            name='Software Engineer'
        )

        self.expect_json_response = {
            'id': 1,
            'name': 'Software Engineer'
        }

    def test_position_response_data(self):
        response = self.client.get(self.detail_paths.build_position_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)
