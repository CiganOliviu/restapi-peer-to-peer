from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.utils import json

from Details.models import HighSchoolProfile, HighSchool, Town, Universitie, Facultie, Domain
from InformaticsDepartment.models import InformaticsGroup
from InformaticsDepartment.tests.test_status_response import InformaticsDepartmentPaths
from Stats.models import Client, Teacher


class InformaticsGroupDataResponseTest(APITestCase):
    def setUp(self):
        self.informatics_department_paths = InformaticsDepartmentPaths()

        User.objects.create_user('client', password='some_random_password')
        User.objects.create_user('teacher', password='some_random_password')

        HighSchoolProfile.objects.create(
            profile='Matematica-Informatica'
        )

        HighSchool.objects.create(
            name='Liceul Teoretic Carei'
        )

        Town.objects.create(
            name='Carei'
        )

        Universitie.objects.create(
            name='UTCN',
            town=Town.objects.get(name='Carei')
        )

        Facultie.objects.create(
            university=Universitie.objects.get(name='UTCN'),
            name='AC'
        )

        Domain.objects.create(
            domain='Informatica'
        )

        Client.objects.create(
            user=User.objects.get(id=1),
            first_name='random_first_name',
            last_name='random_last_name',
            email='random_email@random.random',
            high_school_profile=HighSchoolProfile.objects.get(profile='Matematica-Informatica'),
            high_school=HighSchool.objects.get(name='Liceul Teoretic Carei'),
            city=Town.objects.get(name='Carei'),
            phone_number='0722233444'
        )

        Teacher.objects.create(
            profile='teachers-profile-image/default.jpg',
            user=User.objects.get(id=2),
            first_name='random_first_name',
            last_name='random_last_name',
            age='21',
            email='random_email@random.random',
            phone_number='0722233444',
            faculty=Facultie.objects.get(name='AC'),
            city=Town.objects.get(name='Carei'),
            description='Random Description',
            one_prop_description='Random Description'
        )

        domains = Domain.objects.all()
        teacher_data = Teacher.objects.get(id=1)
        teacher_data.domain_expertise.add(*domains)

        InformaticsGroup.objects.create(
            name='Group 1',
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=2))
        )

        client = Client.objects.filter(id=1)
        informatics_group = InformaticsGroup.objects.get(id=1)
        informatics_group.client.add(*client)

        self.expect_json_response = {
            'id': 1,
            'client': [{
                'id': 1,
                'user': 1,
                'first_name': 'random_first_name',
                'last_name': 'random_last_name',
                'email': 'random_email@random.random',
                'high_school_profile': {'id': 1, 'profile': 'Matematica-Informatica'},
                'high_school': {'id': 1, 'name': 'Liceul Teoretic Carei'},
                'city': {'id': 1, 'name': 'Carei'},
                'phone_number': '0722233444'
            }],
            'name': 'Group 1',
            'responsible_teacher': {
                'id': 1,
                'profile': '/MEDIA/teachers-profile-image/default.jpg',
                'user': 2,
                'first_name': 'random_first_name',
                'last_name': 'random_last_name',
                'age': '21',
                'email': 'random_email@random.random',
                'phone_number': '0722233444',
                'faculty': {
                    'id': 1,
                    'name': 'AC',
                    'university': {
                        'id': 1,
                        'name': 'UTCN',
                        'town': {
                            'id': 1,
                            'name': 'Carei'
                        }
                    }
                },
                'city': {'id': 1, 'name': 'Carei'},
                'domain_expertise': [
                    {
                        'id': 1,
                        'domain': 'Informatica'
                    }
                ],
                'description': 'Random Description',
                'one_prop_description': 'Random Description'
            }
        }

    def test_informatics_group_data(self):
        response = self.client.get(self.informatics_department_paths.build_group_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class InformaticsScheduleDataResponseTest(APITestCase):
    def setUp(self):
        pass

    def test_informatics_schedule_data(self):
        pass


class InformaticsHomeworkDataResponseTest(APITestCase):
    def setUp(self):
        pass

    def test_informatics_homework_data(self):
        pass
