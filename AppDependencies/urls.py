from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('hero-card', views.HeroCardLister.as_view(), name='HeroCardLister'),
    path('hero-card/<int:pk>', views.HeroCardDetail.as_view(), name='HeroCardDetail'),
    path('homework-card', views.HomeworkCardLister.as_view(), name='HomeworkCardLister'),
    path('homework-card/<int:pk>', views.HomeworkCardDetail.as_view(), name='HomeworkCardDetail'),
    path('schedule-card', views.ScheduleCardLister.as_view(), name='ScheduleCardLister'),
    path('schedule-card/<int:pk>', views.ScheduleCardDetail.as_view(), name='ScheduleCardDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
