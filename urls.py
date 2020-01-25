from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from package import views

urlpatterns = [
    path('package/', views.PackageList.as_view(),name='package-list'),
    path('package/<int:pk>/', views.PackageDetail.as_view()),
    # path('pkg/<int:pk>/highlight/', views.PackageHighlight.as_view(), name='package-highlight'),
    path('packagestatus/', views.PackageStatusList.as_view(),name='packagestatus-list'),
    path('packagestatus/<int:pk>/', views.PackageStatusDetail.as_view()),
    # path('ps/<int:pk>/highlight/', views.PackageStatusHighlight.as_view(), name='packagestatus-highlight'),
    path('packagerates/', views.PackageRatesList.as_view(),name='packagerates-list'),
    path('packagerates/<int:pk>/', views.PackageRatesDetail.as_view()),
    path('packagebill/', views.PackageBillingList.as_view(),name='packagebilling-list'),
    path('packagebill/<int:pk>/', views.PackageBillingDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
