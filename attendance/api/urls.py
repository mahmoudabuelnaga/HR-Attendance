from django.urls import path
from .views import AttendanceListAPIView, AttendanceCreateAPIView

urlpatterns = [
    path('', AttendanceListAPIView.as_view()),
    path('create/', AttendanceCreateAPIView.as_view())
]
