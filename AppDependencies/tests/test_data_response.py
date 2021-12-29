from rest_framework.test import APITestCase
from rest_framework.utils import json

from AppDependencies.models import HeroCard, HomeworkCard, ScheduleCard
from AppDependencies.tests.tests_dependencies import AppDependenciesPaths


class HeroCardDataTests(APITestCase):

    def setUp(self):
        self.constants = AppDependenciesPaths()
        HeroCard.objects.create(title='Welcome to PeerToPeer learning',
                                overview='Delivering Experiences That Students Love',
                                image='wallpapers/wallpaper.jpg')

        self.expected_json_response = {
            'id': 1,
            'title': 'Welcome to PeerToPeer learning',
            'overview': 'Delivering Experiences That Students Love',
            'image': '/MEDIA/wallpapers/wallpaper.jpg'
        }

    def test_hero_card_response_data(self):
        response = self.client.get(self.constants.build_hero_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class HomeworkCardTests(APITestCase):

    def setUp(self):
        self.constants = AppDependenciesPaths()
        HomeworkCard.objects.create(alt='Simple homework title',
                                    image='wallpapers/wallpaper.jpg')

        self.expected_json_response = {
            'id': 1,
            'alt': 'Simple homework title',
            'image': '/MEDIA/wallpapers/wallpaper.jpg'
        }

    def test_homework_card_response_data(self):
        response = self.client.get(self.constants.build_homework_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class ScheduleCardTests(APITestCase):

    def setUp(self):
        self.constants = AppDependenciesPaths()
        ScheduleCard.objects.create(alt='Simple schedule title',
                                    image='wallpapers/wallpaper.jpg')

        self.expected_json_response = {
            'id': 1,
            'alt': 'Simple schedule title',
            'image': '/MEDIA/wallpapers/wallpaper.jpg'
        }

    def test_schedule_card_response_data(self):
        response = self.client.get(self.constants.build_schedule_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)
