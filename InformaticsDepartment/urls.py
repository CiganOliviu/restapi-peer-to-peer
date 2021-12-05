from django.urls import path
from InformaticsDepartment import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('informatics-group', views.InformaticsGroupLister.as_view(),
         name='InformaticsGroupLister'),
    path('informatics-group/<int:pk>', views.InformaticsGroupDetails.as_view(),
         name='InformaticsGroupDetails'),

    path('informatics-schedule', views.InformaticsScheduleLister.as_view(),
         name='InformaticsScheduleLister'),
    path('informatics-schedule/<int:pk>', views.InformaticsScheduleDetails.as_view(),
         name='InformaticsScheduleDetails'),

    path('informatics-homework', views.InformaticsHomeworkLister.as_view(),
         name='InformaticsHomeworkLister'),
    path('informatics-homework/<int:pk>', views.InformaticsHomeworkDetails.as_view(),
         name='InformaticsHomeworkDetails'),
]
urlpatterns = format_suffix_patterns(urlpatterns)


