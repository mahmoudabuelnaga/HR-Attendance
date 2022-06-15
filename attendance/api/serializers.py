from genericpath import exists
from rest_framework import serializers
from attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'employee_name', 'date', 'from_time', 'to_time']
        
    
class AttendanceSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'date', 'from_time', 'to_time']

    def validate(self, data):
        """
        Validation of start and end date.
        """
        date = data['date']
        start_date = data['from_time']
        end_date = data['to_time']
        if Attendance.objects.filter(
            employee_name=self.context['request'].user,
            date=date, from_time=start_date, 
            to_time=end_date
            ).exists():
            raise serializers.ValidationError("No attendance interval overlapping is allowed.")

        if start_date > end_date:
            raise serializers.ValidationError("Check-out can't be before check-in.")

        return data