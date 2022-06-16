from rest_framework import generics
from attendance.models import Attendance
from .serializers import AttendanceSerializer, AttendanceSerializerForCreate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework


class AttendanceListAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['employee_name', 'date', 'arrived_late', 'leave_early']
    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_staff and self.request.user.is_superuser: # is_superuser , is_active
            print(self.request.user)
            qs = Attendance.objects.all()
        else:
            qs = Attendance.objects.filter(employee_name=user).all()
        return qs



class AttendanceCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AttendanceSerializerForCreate
    
    def perform_create(self, serializer):
        serializer.save(employee_name=self.request.user)

        