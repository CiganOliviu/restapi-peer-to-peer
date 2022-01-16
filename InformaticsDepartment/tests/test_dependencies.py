class InformaticsDepartmentPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/informatics'
        self.__GROUP_URL = '/informatics-group'
        self.__SCHEDULE_URL = '/informatics-schedule'
        self.__HOMEWORK_URL = '/informatics-homework'

    def build_group_url(self):
        return self.__STANDARD_BACKEND_URL + self.__GROUP_URL

    def build_schedule_url(self):
        return self.__STANDARD_BACKEND_URL + self.__SCHEDULE_URL

    def build_homework_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOMEWORK_URL


class InformaticsDepartmentExpectedJsonResponses:
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

    @staticmethod
    def get_schedule_data_expected_json_response():
        return {
            'id': 1,
            'course_title': 'Programare Dinamica',
            'teacher': {"email": "", "first_name": "", "id": 1, "last_name": ""},
            'group': {
                'id': 1,
                'client': [{
                    'id': 1,
                    'user': 2,
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
                    'user': 1,
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
            'title': 'Programarea Calculatoarelor',
            'groups': [
                {
                    'id': 1,
                    'client': [{
                        'id': 1,
                        'user': 2,
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
                        'user': 1,
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
            ],
            'file': '/MEDIA/homeworks/informatics/homework.pdf',
            'tips': 'None',
            'optional': False,
            'deadline_date': '2023-10-19',
            'deadline_hour': '10:33:45',
            'dated': False,
            'posted_on': '2021-10-19'
        }
