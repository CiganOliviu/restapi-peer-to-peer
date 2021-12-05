from knox import views as knox_views
from django.urls import path
from Details import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('domain', views.DomainLister.as_view(), name='DomainLister'),
    path('domain/<int:pk>', views.DomainDetail.as_view(), name='DomainDetail'),

    path('high-school-profile', views.HighSchoolProfileLister.as_view(), name='HighSchoolProfileLister'),
    path('high-school-profile/<int:pk>', views.HighSchoolProfileDetail.as_view(), name='HighSchoolProfileDetail'),

    path('high-school', views.HighSchoolLister.as_view(), name='HighSchoolLister'),
    path('high-school/<int:pk>', views.HighSchoolDetail.as_view(), name='HighSchoolDetail'),

    path('town', views.TownLister.as_view(), name='TownLister'),
    path('town/<int:pk>', views.TownDetail.as_view(), name='TownDetail'),

    path('university', views.UniversitieLister.as_view(), name='UniversitieLister'),
    path('university/<int:pk>', views.UniversitiesDetail.as_view(), name='UniversityDetail'),

    path('faculty', views.FacultieLister.as_view(), name='FacultieLister'),
    path('faculty/<int:pk>', views.FacultieDetail.as_view(), name='FacultieDetail'),

    path('position', views.PositionLister.as_view(), name='PositionLister'),
    path('position/<int:pk>', views.PositionDetail.as_view(), name='PositionDetail'),

    path('user', views.UserLister.as_view(), name='UserLister'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='UserDetail'),

    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
