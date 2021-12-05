from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('client', views.ClientLister.as_view(), name='ClientLister'),
    path('client/<int:pk>', views.ClientDetails.as_view(), name='ClientDetails'),

    path('teacher', views.TeacherLister.as_view(), name='TeacherLister'),
    path('teacher/<int:pk>', views.TeacherDetails.as_view(), name='TeacherDetails'),

    path('staff', views.StaffLister.as_view(), name='StaffLister'),
    path('staff/<int:pk>', views.StaffDetails.as_view(), name='StaffDetails'),

    path('income', views.IncomeLister.as_view(), name='IncomeLister'),
    path('income/<int:pk>', views.IncomeDetails.as_view(), name='IncomeDetails'),

    path('expense', views.ExpenseLister.as_view(), name='ExpenseLister'),
    path('expense/<int:pk>', views.ExpenseDetails.as_view(), name='ExpenseDetails'),

    path('feedback', views.FeedbackLister.as_view(), name='FeedbackLister'),
    path('feedback/<int:pk>', views.FeedbackDetails.as_view(), name='FeedbackDetails'),

    path('teacher-expectations', views.TeacherExpectationLister.as_view(),
         name='TeacherExpectationLister'),
    path('teacher-expectations/<int:pk>', views.TeacherExpectationDetails.as_view(),
         name='TeacherExpectationDetails'),

    path('student-expectations', views.StudentExpectationLister.as_view(),
         name='StudentExpectationLister'),
    path('student-expectations/<int:pk>', views.StudentExpectationDetails.as_view(),
         name='StudentExpectationDetails'),
]
urlpatterns = format_suffix_patterns(urlpatterns)


