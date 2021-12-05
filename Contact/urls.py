from django.urls import path
from . import views


urlpatterns = [
    path('contact-lister', views.ContactLister.as_view(), name='ClientLister'),
    path('contact-lister/<int:pk>', views.ContactDetails.as_view(), name='ClientDetails'),
]
