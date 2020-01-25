from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from location import views

urlpatterns = [

    path('franchise', views.FranchiseList.as_view(),name='franchise-list'),
    path('franchise/<int:pk>/' ,views.FranchiseDetail.as_view()),
    path('location', views.LocationList.as_view(),name='location-list'),
    path('location/<int:pk>/' ,views.LocationDetail.as_view()),
    path('locationtype/', views.LocationTypeList.as_view(), name='locationtype-list'),
    path('locationtype/<int:pk>/', views.LocationTypeDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)
