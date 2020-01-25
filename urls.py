from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views

urlpatterns = [
    path('vehicle/', views.VehicleList.as_view(),name='vehicle-list'),
    path('vehicle/<int:pk>/', views.VehicleDetail.as_view()),
    path('vehicletype/', views.VehicleTypeList.as_view(),name='vehicletype-list'),
    path('vehicletype/<int:pk>/', views.VehicleTypeDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
