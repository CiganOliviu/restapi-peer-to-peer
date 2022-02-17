from rest_framework.test import APITestCase
from rest_framework.utils import json

from AppLayout.models import HeroCard, HomeworkCard, ScheduleCard, ContentSection, ContentWithImagesSection, HomeContent
from AppLayout.tests.tests_dependencies import AppDependenciesPaths, AppDependenciesExpectedJsonResponses

app_dependencies_paths = AppDependenciesPaths()
app_dependencies_json_responses = AppDependenciesExpectedJsonResponses()


class HeroCardDataTests(APITestCase):

    def setUp(self):
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
        response = self.client.get(app_dependencies_paths.build_hero_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class HomeworkCardTests(APITestCase):

    def setUp(self):
        HomeworkCard.objects.create(alt='Simple homework title',
                                    image='wallpapers/wallpaper.jpg')

        self.expected_json_response = {
            'id': 1,
            'alt': 'Simple homework title',
            'image': '/MEDIA/wallpapers/wallpaper.jpg'
        }

    def test_homework_card_response_data(self):
        response = self.client.get(app_dependencies_paths.build_homework_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class ScheduleCardTests(APITestCase):

    def setUp(self):
        ScheduleCard.objects.create(alt='Simple schedule title',
                                    image='wallpapers/wallpaper.jpg')

        self.expected_json_response = {
            'id': 1,
            'alt': 'Simple schedule title',
            'image': '/MEDIA/wallpapers/wallpaper.jpg'
        }

    def test_schedule_card_response_data(self):
        response = self.client.get(app_dependencies_paths.build_schedule_card_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class ContentSectionTests(APITestCase):
    def setUp(self):
        ContentSection.objects.create(title='Content Section Title',
                                      content='Content Section Content')

        self.expected_json_response = {
            'id': 1,
            'title': 'Content Section Title',
            'content': 'Content Section Content',
        }

    def test_content_section_response_data(self):
        response = self.client.get(app_dependencies_paths.build_content_section_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class ContentImageSectionTests(APITestCase):
    def setUp(self):
        ContentWithImagesSection.objects.create(image='app-layout/ContentWithImages/wallpaper.jpg',
                                                title='Content Image Section Title',
                                                content='Content Image Section Content')

        self.expected_json_response = {
            'id': 1,
            'image': '/MEDIA/app-layout/ContentWithImages/wallpaper.jpg',
            'title': 'Content Image Section Title',
            'content': 'Content Image Section Content',
        }

    def test_content_section_with_images_response_data(self):
        response = self.client.get(app_dependencies_paths.build_content_image_section_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class HomeContentTests(APITestCase):
    def setUp(self):
        ContentSection.objects.create(title='Content Section Title One',
                                      content='Content Section Content One')

        ContentSection.objects.create(title='Content Section Title Two',
                                      content='Content Section Content Two')

        ContentWithImagesSection.objects.create(image='app-layout/ContentWithImages/wallpaper_one.jpg',
                                                title='Content Image Section Title One',
                                                content='Content Image Section Content One')

        ContentWithImagesSection.objects.create(image='app-layout/ContentWithImages/wallpaper_two.jpg',
                                                title='Content Image Section Title Two',
                                                content='Content Image Section Content Two')

        ContentWithImagesSection.objects.create(image='app-layout/ContentWithImages/wallpaper_three.jpg',
                                                title='Content Image Section Title Three',
                                                content='Content Image Section Content Three')

        HomeContent.objects.create(config_title='Config title',
                                   section_one_title_content=ContentSection.objects.get(id=1),
                                   section_two_title_content=ContentSection.objects.get(id=2),
                                   section_one_with_images_content=ContentWithImagesSection.objects.get(id=1),
                                   section_two_with_images_content=ContentWithImagesSection.objects.get(id=2),
                                   section_three_with_images_content=ContentWithImagesSection.objects.get(id=3))

        self.expected_json_response = app_dependencies_json_responses.get_home_content_expected_json_response()

    def test_home_content_response_data(self):
        response = self.client.get(app_dependencies_paths.build_home_content_url(), format='json',
                                   content_type='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)
