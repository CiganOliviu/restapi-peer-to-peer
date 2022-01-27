class RomanianDepartmentPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/romanian'
        self.__GROUP_URL = '/romanian-group'
        self.__SCHEDULE_URL = '/romanian-schedule'
        self.__HOMEWORK_URL = '/romanian-homework'

    def build_group_url(self):
        return self.__STANDARD_BACKEND_URL + self.__GROUP_URL

    def build_schedule_url(self):
        return self.__STANDARD_BACKEND_URL + self.__SCHEDULE_URL

    def build_homework_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOMEWORK_URL


class RomanianDepartmentExpectedJsonResponses:
    @staticmethod
    def get_group_data_expected_json_response():
        return {
            'id': 1,
            'client': [{
                'id': 1,
                'user': 1,
                'first_name': 'random_first_name',
                'last_name': 'random_last_name',
                'email': 'random_email@random.random',
                'high_school_profile': {'id': 1, 'profile': 'Matematica-Informatica'},
                'high_school': {'id': 1, 'name': 'Colegiul National Mihai Eminescu'},
                'city': {'id': 1, 'name': 'Cluj-Napoca'},
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
                    'name': 'Automatica si Calculatoare',
                    'university': {
                        'id': 1,
                        'name': 'Universitatea Tehnica',
                        'town': {
                            'id': 1,
                            'name': 'Cluj-Napoca'
                        }
                    }
                },
                'city': {'id': 1, 'name': 'Cluj-Napoca'},
                'domain_expertise': [
                    {
                        'id': 1,
                        'domain': 'Matematica'
                    }
                ],
                'description': 'Random Description',
                'one_prop_description': 'Random Description'
            }
        }

    @staticmethod
    def get_schedule_data_expected_json_response():
        return {
            'id': 1,
            'course_title': 'ION',
            'teacher': {"email": "", "first_name": "", "id": 1, "last_name": ""},
            'group': {
                'id': 1,
                'client': [{
                    'id': 1,
                    'user': 2,
                    'first_name': 'random_first_name',
                    'last_name': 'random_last_name',
                    'email': 'random_email@random.random',
                    'high_school_profile': {'id': 1, 'profile': 'Stiinte ale Naturii'},
                    'high_school': {'id': 1, 'name': 'Doamna Stanca'},
                    'city': {'id': 1, 'name': 'Cluj-Napoca'},
                    'phone_number': '0722233444'
                }],
                'name': 'Group 1',
                'responsible_teacher': {
                    'id': 1,
                    'profile': '/MEDIA/teachers-profile-image/default.jpg',
                    'user': 1,
                    'first_name': 'random_first_name',
                    'last_name': 'random_last_name',
                    'age': '21',
                    'email': 'random_email@random.random',
                    'phone_number': '0722233444',
                    'faculty': {
                        'id': 1,
                        'name': 'Automation and Applied Informatics',
                        'university': {
                            'id': 1,
                            'name': 'Tehnical University',
                            'town': {
                                'id': 1,
                                'name': 'Cluj-Napoca'
                            }
                        }
                    },
                    'city': {'id': 1, 'name': 'Cluj-Napoca'},
                    'domain_expertise': [
                        {
                            'id': 1,
                            'domain': 'Limba Romana'
                        }
                    ],
                    'description': 'Random Description',
                    'one_prop_description': 'Random Description'
                }
            },
            'deadline_date': '2023-10-19',
            'deadline_hour': '10:33:45',
            'dated': False,
            'posted_on': '2021-10-19'
        }

    @staticmethod
    def get_homework_data_expected_json_response():
        return {
            'id': 1,
            'teacher': {"email": "", "first_name": "", "id": 1, "last_name": ""},
            'title': 'Programare Functionala',
            'groups': [
                {
                    'id': 1,
                    'client': [{
                        'id': 1,
                        'user': 2,
                        'first_name': 'random_first_name',
                        'last_name': 'random_last_name',
                        'email': 'random_email@random.random',
                        'high_school_profile': {'id': 1, 'profile': 'Informatica intensiva'},
                        'high_school': {'id': 1, 'name': 'Cambridge High-School'},
                        'city': {'id': 1, 'name': 'Harvard'},
                        'phone_number': '0722233444'
                    }],
                    'name': 'Group 1',
                    'responsible_teacher': {
                        'id': 1,
                        'profile': '/MEDIA/teachers-profile-image/default.jpg',
                        'user': 1,
                        'first_name': 'random_first_name',
                        'last_name': 'random_last_name',
                        'age': '21',
                        'email': 'random_email@random.random',
                        'phone_number': '0722233444',
                        'faculty': {
                            'id': 1,
                            'name': 'Computer Science',
                            'university': {
                                'id': 1,
                                'name': 'Harvard University',
                                'town': {
                                    'id': 1,
                                    'name': 'Harvard'
                                }
                            }
                        },
                        'city': {'id': 1, 'name': 'Harvard'},
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
            ],
            'file': '/MEDIA/homeworks/mathematics/homework.pdf',
            'tips': 'None',
            'optional': False,
            'deadline_date': '2023-10-19',
            'deadline_hour': '10:33:45',
            'dated': False,
            'posted_on': '2021-10-19'
        }