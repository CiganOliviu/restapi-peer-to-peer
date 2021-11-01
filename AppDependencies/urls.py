from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('hero-card', views.HeroCardLister.as_view(), name='HeroCardLister'),
    path('hero-card/<int:pk>', views.HeroCardDetail.as_view(), name='HeroCardDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
