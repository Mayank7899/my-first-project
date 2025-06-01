from django.urls import path
from testproject.views import RegisterUser
from .views import *

urlpatterns = [
    path('destinations/', DestinationListCreate.as_view(), name='destination-list-create'),
    path('trips/', TripListCreate.as_view(), name='trip-list-create'),
    path('trips/<int:pk>/', TripDetail.as_view()),
    path('bookings/', BookingListCreate.as_view()),
    path('bookings/<int:pk>/', BookingDetail.as_view()),
    path('register/', RegisterUser.as_view(), name='register'),
]