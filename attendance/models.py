from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)  # New field to identify the service
    time = models.IntegerField(choices=(
        (7, '7 AM - General Service'),
        (9, '9 AM - General Service'),
        (13, '1 PM - Youth Service'),
        (1, ('Others - Campus Service'))
    ))

    def __str__(self):
        return f"{self.name} at {dict(self.time.choices)[self.time]}"


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField()
    age = models.IntegerField()
    fb_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)  # Allow null temporarily
    status = models.BooleanField(default=False)

    def __str__(self):
        service_str = self.service.name if self.service else "No Service"
        return f"{self.member} - {service_str} - {self.date} - {'Present' if self.status else 'Absent'}"

class Ministers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)


    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"