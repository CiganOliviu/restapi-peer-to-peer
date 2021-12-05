from django.contrib import admin
from Contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', 'subject')
    filter = ('email', 'date')


admin.site.register(Contact, ContactAdmin)
