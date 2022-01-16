import datetime

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.utils import json

from Details.models import HighSchoolProfile, HighSchool, Town, Universitie, Facultie, Domain
from InformaticsDepartment.models import InformaticsGroup, InformaticsSchedule, InformaticsHomework
from InformaticsDepartment.tests.test_dependencies import InformaticsDepartmentExpectedJsonResponses
from InformaticsDepartment.tests.test_dependencies import InformaticsDepartmentPaths
from Stats.models import Client, Teacher

informatics_department_paths = InformaticsDepartmentPaths()
informatics_department_json_responses = InformaticsDepartmentExpectedJsonResponses()


class InformaticsGroupDataResponseTest(APITestCase):
    def setUp(self):
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

        self.expect_json_response = informatics_department_json_responses.get_group_data_expected_json_response()

    def test_informatics_group_data(self):
        response = self.client.get(informatics_department_paths.build_group_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class InformaticsScheduleDataResponseTest(APITestCase):
    def setUp(self):
        User.objects.create_user('teacher', password='some_random_password')
        User.objects.create_user('client', password='some_random_password')

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

        HighSchoolProfile.objects.create(
            profile='Matematica-Informatica'
        )

        HighSchool.objects.create(
            name='Liceul Teoretic Carei'
        )

        Domain.objects.create(
            domain='Informatica'
        )

        Client.objects.create(
            user=User.objects.get(id=2),
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
            user=User.objects.get(id=1),
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
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=1))
        )

        client = Client.objects.filter(id=1)
        informatics_group = InformaticsGroup.objects.get(id=1)
        informatics_group.client.add(*client)

        InformaticsSchedule.objects.create(
            course_title='Programare Dinamica',
            teacher=User.objects.get(id=1),
            group=InformaticsGroup.objects.get(id=1),
            deadline_date=datetime.date(2023, 10, 19),
            deadline_hour=datetime.time(10, 33, 45),
            dated=False,
            posted_on=datetime.date(2021, 10, 19)
        )

        self.expect_json_response = informatics_department_json_responses.\
            get_schedule_data_expected_json_response()

    def test_informatics_schedule_data(self):
        response = self.client.get(informatics_department_paths.build_schedule_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)


class InformaticsHomeworkDataResponseTest(APITestCase):
    def setUp(self):
        User.objects.create_user('teacher', password='some_random_password')
        User.objects.create_user('client', password='some_random_password')

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

        HighSchoolProfile.objects.create(
            profile='Matematica-Informatica'
        )

        HighSchool.objects.create(
            name='Liceul Teoretic Carei'
        )

        Domain.objects.create(
            domain='Informatica'
        )

        Client.objects.create(
            user=User.objects.get(id=2),
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
            user=User.objects.get(id=1),
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
            responsible_teacher=Teacher.objects.get(user=User.objects.get(id=1))
        )

        client = Client.objects.filter(id=1)
        informatics_group = InformaticsGroup.objects.get(id=1)
        informatics_group.client.add(*client)

        InformaticsHomework.objects.create(
            teacher=User.objects.get(id=1),
            title='Programarea Calculatoarelor',
            file='homeworks/informatics/homework.pdf',
            tips='None',
            optional=False,
            deadline_date=datetime.date(2023, 10, 19),
            deadline_hour=datetime.time(10, 33, 45),
            dated=False,
            posted_on=datetime.date(2021, 10, 19),
        )

        groups = InformaticsGroup.objects.all()
        homeworks = InformaticsHomework.objects.get(id=1)
        homeworks.groups.add(*groups)

        self.expect_json_response = informatics_department_json_responses.\
            get_homework_data_expected_json_response()

    def test_informatics_homework_data(self):
        response = self.client.get(informatics_department_paths.build_homework_url(), format='json',
                                   content_filter='application/json')

        response_data_as_json = json.dumps(response.data[0], sort_keys=True)
        expected_response_data_as_json = json.dumps(self.expect_json_response, sort_keys=True)

        self.assertEqual(response_data_as_json, expected_response_data_as_json)
