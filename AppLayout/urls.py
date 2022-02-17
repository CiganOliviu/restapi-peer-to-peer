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
    path('content-section', views.ContentSectionLister.as_view(), name='ContentSectionLister'),
    path('content-section/<int:pk>', views.ContentSectionDetail.as_view(), name='ContentSectionDetail'),
    path('content-images-section', views.ContentWithImagesSectionLister.as_view(),
         name='ContentWithImagesSectionLister'),
    path('content-images-section/<int:pk>', views.ContentWithImagesSectionDetail.as_view(),
         name='ContentWithImagesSectionDetail'),
    path('home-content', views.HomeContentLister.as_view(), name='HomeContentLister'),
    path('home-content/<int:pk>', views.HomeContentDetail.as_view(), name='HomeContentDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
