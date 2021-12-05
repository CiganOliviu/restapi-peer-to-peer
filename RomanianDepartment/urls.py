from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from RomanianDepartment import views

urlpatterns = [
    path('romanian-group', views.RomanianGroupLister.as_view(),
         name='RomanianGroupLister'),
    path('romanian-group/<int:pk>', views.RomanianGroupDetails.as_view(),
         name='RomanianGroupDetails'),

    path('romanian-schedule', views.RomanianScheduleLister.as_view(),
         name='RomanianScheduleLister'),
    path('romanian-schedule/<int:pk>', views.RomanianScheduleDetails.as_view(),
         name='RomanianScheduleDetails'),

    path('romanian-homework', views.RomanianHomeworkLister.as_view(),
         name='RomanianHomeworkLister'),
    path('romanian-homework/<int:pk>', views.RomanianHomeworkDetails.as_view(),
         name='RomanianHomeworkDetails'),
]
urlpatterns = format_suffix_patterns(urlpatterns)


