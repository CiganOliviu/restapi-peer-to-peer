class ContactPaths:
    def __init__(self):
        self.STANDARD_BACKEND_URL = 'http://localhost:8000/contact'
        self.CONTACT_URL = '/contact-lister'

    def build_contact_url(self):
        return self.STANDARD_BACKEND_URL + self.CONTACT_URL
