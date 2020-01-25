from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from USer import views

urlpatterns = [
    path('user/', views.USerList.as_view(), name='user-list'),
    path('user<int:pk>/', views.USerDetail.as_view()),
    path('usertype/', views.UserTypeList.as_view(),name='usertype-list'),
    path('usertype/<int:pk>/', views.UserTypeDetail.as_view()),
    # path('sender/', views.SenderList.as_view(),name='sender-list'),
    # path('sender/<int:pk>/', views.SenderDetail.as_view(),),
    # path('receiver/', views.ReceiverList.as_view(),name='receiver-list'),
    # path('receiver<int:pk>/', views.ReceiverDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
    path('man/', views.ManagerList.as_view(),name='man-list'),
    path('man<int:pk>/', views.ManagerDetail.as_view()),
    path('post/', views.PostPersonList.as_view(),name='post-list'),
    path('post<int:pk>/', views.PostPersonDetail.as_view()),
    path('staff/', views.StaffList.as_view(),name='staff-list'),
    path('staff<int:pk>/', views.StaffDetail),
"""