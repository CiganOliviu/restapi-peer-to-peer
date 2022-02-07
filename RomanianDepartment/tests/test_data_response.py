import json
import datetime

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from Details.models import HighSchoolProfile, HighSchool, Town, Universitie, Facultie, Domain
from RomanianDepartment.models import RomanianGroup, RomanianSchedule, RomanianHomework
from RomanianDepartment.tests.test_dependencies import RomanianDepartmentPaths, RomanianDepartmentExpectedJsonResponses
from Stats.models import Client, Teacher

romanian_department_paths = RomanianDepartmentPaths()
romanian_department_json_responses = RomanianDepartmentExpectedJsonResponses()


class RomanianGroupDataResponseTest(APITestCase):
    def setUp(self):
        User.objects.create_user('client', password='some_random_password')
        User.objects.create_user('teacher', password='some_random_password')

        HighSchoolProfile.objects.create(
            profile='Matematica-Informatica'
        )

        HighSchool.objects.create(
            name='Colegiul National Mihai Eminescu'
        )

        Town.objects.create(
            name='Cluj-Napoca'
        )

        Universitie.objects.create(
            name='Universitatea Tehnica',
            town=Town.objects.get(name='Cluj-Napoca')
        )

        Facultie.objects.create(
            university=Universitie.objects.get(name='Universitatea Tehnica'),
            name='Automatica si Calculatoare'
        )

        Domain.objects.create(
            domain='Matematica'
        )

        Client.objects.create(
            user=User.objects.get(id=1),
            first_name='random_first_name',
            last_name='random_last_name',
            email='random_email@random.random',
            high_school_profile=HighSchoolProfile.objects.get(profile='Matematica-Informatica'),
            high_school=HighSchool.objects.get(name='Colegiul National Mihai Eminescu'),
            city=Town.objects.get(name='Cluj-Napoca'),
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
            faculty=Facultie.objects.get(name='Automatica si Calculatoare'),
            city=Town.objects.get(name='Cluj-Napoca'),
            description='Random Description',
            one_prop_description='Random Description'
        )

        domains = Domain.objects.all()
        teacher_data = Teacher.objects.get(id=1)
        teacher_data.domain_expertise.add(*domains)

        RomanianGroup.objects.create(
            name='Group 1',
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=2))
        )

        client = Client.objects.filter(id=1)
        romanian_group = RomanianGroup.objects.get(id=1)
        romanian_group.client.add(*client)

        self.expected_json_response = romanian_department_json_responses.get_group_data_expected_json_response()

    def test_romanian_group_data(self):
        response = self.client.get(romanian_department_paths.build_group_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_data_as_json)


class RomanianScheduleDataResponseTest(APITestCase):
    def setUp(self):
        User.objects.create_user('teacher', password='some_random_password')
        User.objects.create_user('client', password='some_random_password')

        Town.objects.create(
            name='Cluj-Napoca'
        )

        Universitie.objects.create(
            name='Tehnical University',
            town=Town.objects.get(name='Cluj-Napoca')
        )

        Facultie.objects.create(
            university=Universitie.objects.get(name='Tehnical University'),
            name='Automation and Applied Informatics'
        )

        HighSchoolProfile.objects.create(
            profile='Stiinte ale Naturii'
        )

        HighSchool.objects.create(
            name='Doamna Stanca'
        )

        Domain.objects.create(
            domain='Limba Romana'
        )

        Client.objects.create(
            user=User.objects.get(id=2),
            first_name='random_first_name',
            last_name='random_last_name',
            email='random_email@random.random',
            high_school_profile=HighSchoolProfile.objects.get(profile='Stiinte ale Naturii'),
            high_school=HighSchool.objects.get(name='Doamna Stanca'),
            city=Town.objects.get(name='Cluj-Napoca'),
            phone_number='0722233444'
        )

        Teacher.objects.create(
            profile='teachers-profile-image/default.jpg',
            user=User.objects.get(id=1),
            first_name='random_first_name',
            last_name='random_last_name',
            age='21',
            email='random_email@random.random',
            phone_number='0722233444',
            faculty=Facultie.objects.get(name='Automation and Applied Informatics'),
            city=Town.objects.get(name='Cluj-Napoca'),
            description='Random Description',
            one_prop_description='Random Description'
        )

        domains = Domain.objects.all()
        teacher_data = Teacher.objects.get(id=1)
        teacher_data.domain_expertise.add(*domains)

        RomanianGroup.objects.create(
            name='Group 1',
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=1))
        )

        client = Client.objects.filter(id=1)
        romanian_groups = RomanianGroup.objects.get(id=1)
        romanian_groups.client.add(*client)

        RomanianSchedule.objects.create(
            course_title='ION',
            teacher=User.objects.get(id=1),
            group=RomanianGroup.objects.get(id=1),
            deadline_date=datetime.date(2023, 10, 19),
            deadline_hour=datetime.time(10, 33, 45),
            dated=False,
            posted_on=datetime.date(2021, 10, 19),
        )

        self.expected_json_response = romanian_department_json_responses.get_schedule_data_expected_json_response()

    def test_romanian_schedule_data(self):
        response = self.client.get(romanian_department_paths.build_schedule_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class RomanianHomeworkDataResponse(APITestCase):
    def setUp(self):
        User.objects.create_user('teacher', password='some_random_password')
        User.objects.create_user('client', password='some_random_password')

        Town.objects.create(
            name='Harvard'
        )

        Universitie.objects.create(
            name='Harvard University',
            town=Town.objects.get(name='Harvard')
        )

        Facultie.objects.create(
            university=Universitie.objects.get(name='Harvard University'),
            name='Computer Science'
        )

        HighSchoolProfile.objects.create(
            profile='Informatica intensiva'
        )

        HighSchool.objects.create(
            name='Cambridge High-School'
        )

        Domain.objects.create(
            domain='Informatica'
        )

        Client.objects.create(
            user=User.objects.get(id=2),
            first_name='random_first_name',
            last_name='random_last_name',
            email='random_email@random.random',
            high_school_profile=HighSchoolProfile.objects.get(profile='Informatica intensiva'),
            high_school=HighSchool.objects.get(name='Cambridge High-School'),
            city=Town.objects.get(name='Harvard'),
            phone_number='0722233444'
        )

        Teacher.objects.create(
            profile='teachers-profile-image/default.jpg',
            user=User.objects.get(id=1),
            first_name='random_first_name',
            last_name='random_last_name',
            age='21',
            email='random_email@random.random',
            phone_number='0722233444',
            faculty=Facultie.objects.get(name='Computer Science'),
            city=Town.objects.get(name='Harvard'),
            description='Random Description',
            one_prop_description='Random Description'
        )

        domains = Domain.objects.all()
        teacher_data = Teacher.objects.get(id=1)
        teacher_data.domain_expertise.add(*domains)

        RomanianGroup.objects.create(
            name='Group 1',
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=1))
        )

        client = Client.objects.filter(id=1)
        romanian_groups = RomanianGroup.objects.get(id=1)
        romanian_groups.client.add(*client)

        RomanianHomework.objects.create(
            teacher=User.objects.get(id=1),
            title='Programare Functionala',
            file='homeworks/mathematics/homework.pdf',
            tips='None',
            optional=False,
            deadline_date=datetime.date(2023, 10, 19),
            deadline_hour=datetime.time(10, 33, 45),
            dated=False,
            posted_on=datetime.date(2021, 10, 19),
        )

        groups = RomanianGroup.objects.all()
        homeworks = RomanianHomework.objects.get(id=1)
        homeworks.groups.add(*groups)

        self.expected_json_response = romanian_department_json_responses.get_homework_data_expected_json_response()

    def test_romanian_homework_data(self):
        response = self.client.get(romanian_department_paths.build_homework_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expected_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)

