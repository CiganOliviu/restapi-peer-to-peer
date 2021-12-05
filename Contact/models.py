from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, default=None, blank=False, null=True)
    last_name = models.CharField(max_length=50, default=None, blank=False, null=True)
    email = models.EmailField(max_length=50, default=None, blank=False, null=True)
    client_type = models.CharField(max_length=50, default=None, blank=False, null=True)
    subject = models.CharField(max_length=50, default=None, blank=False, null=True)
    phone_number = models.CharField(max_length=50, default="07 XXX XXX XX", blank=False)
    message = models.TextField(default=None, blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


