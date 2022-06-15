from datetime import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from datetime import time
import datetime
import pandas as pd

# Create your models here.

class Attendance(models.Model):
    
    employee_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    arrived_late = models.BooleanField(default=False)
    leave_early = models.BooleanField(default=False)
    working_hours = models.CharField(max_length=20)
    overtime_working_hours = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.employee_name} - {self.date} - {self.from_time} - {self.to_time}"


    def save(self, *args, **kwargs):
        start_time_hour = f"{self.from_time.hour}"
        end_time_hour = f"{self.to_time.hour}"
        if self.from_time.minute == 0:
            start_time = int(start_time_hour)
        else:
            start_time_minute = self.from_time.minute
            Percentage_of_minutes = start_time_minute/60
            start_time_str = f"{start_time_hour}"
            start_time = float(start_time_str)+Percentage_of_minutes
        if self.to_time.minute == 0:
            end_time = int(end_time_hour)
        else:
            end_time_minute = self.to_time.minute
            Percentage_of_minutes = end_time_minute/60
            end_time_str = f"{end_time_hour}"
            end_time = float(end_time_str)+Percentage_of_minutes

        ##################################################################################
        full_time = end_time - start_time
        temp = pd.Timestamp(f"{self.date}")

        if temp.day_name() in ['Friday', 'Saturday']:
            overtime = (full_time * 3600)
            self.working_hours = str(datetime.timedelta(seconds = 0))
            self.overtime_working_hours = str(datetime.timedelta(seconds = overtime))

        elif full_time > 8:
            overtime = (full_time - 8) * 3600
            self.working_hours = str(datetime.timedelta(seconds = 28800))
            self.overtime_working_hours = str(datetime.timedelta(seconds = overtime))
        
        else:
            f_time = full_time * 3600
            self.working_hours = str(datetime.timedelta(seconds = f_time))
            self.overtime_working_hours = str(datetime.timedelta(seconds = 0))

        ##################################################################################
        if self.from_time > time(9, 00, 00):
            self.arrived_late = True
        
        if self.to_time < time(17, 00, 00):
            self.leave_early = True

        super(Attendance, self).save(*args, **kwargs)


