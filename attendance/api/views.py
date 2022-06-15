from rest_framework import generics
from attendance.models import Attendance
from .serializers import AttendanceSerializer, AttendanceSerializerForCreate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework


class AttendanceListAPIView(generics.ListAPIView):
    # queryset = Attendance.objects.filter(employee_name='')
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
    # serializer_class = AttendanceSerializerForCreate
    permission_classes = [IsAuthenticated]
    serializer_class = AttendanceSerializerForCreate
    # def get_serializer(self, *args, **kwargs):
    #     """
    #     Return the serializer instance that should be used for validating and
    #     deserializing input, and for serializing output.
    #     """
        # if self.request.user.is_staff and self.request.user.is_superuser: # is_superuser , is_active
        #     serializer_class = AttendanceSerializer
        # else:
        # serializer_class = AttendanceSerializerForCreate
        # kwargs.setdefault('context', self.get_serializer_context())
        # return serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        # if self.request.user.is_staff and self.request.user.is_superuser: # is_superuser , is_active
        #     serializer.save()
           
        # else:
        serializer.save(employee_name=self.request.user)

        