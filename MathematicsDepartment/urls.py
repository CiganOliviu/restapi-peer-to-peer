from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('mathematics-group', views.MathematicsGroupLister.as_view(),
         name='MathematicsGroupLister'),
    path('mathematics-group/<int:pk>', views.MathematicsGroupDetails.as_view(),
         name='MathematicsGroupDetails'),

    path('mathematics-schedule', views.MathematicsScheduleLister.as_view(),
         name='MathematicsScheduleLister'),
    path('mathematics-schedule/<int:pk>', views.MathematicsScheduleDetails.as_view(),
         name='MathematicsScheduleDetails'),

    path('mathematics-homework', views.MathematicsHomeworkLister.as_view(),
         name='MathematicsHomeworkLister'),
    path('mathematics-schedule/<int:pk>', views.MathematicsScheduleDetails.as_view(),
         name='MathematicsScheduleDetails'),
]
urlpatterns = format_suffix_patterns(urlpatterns)


