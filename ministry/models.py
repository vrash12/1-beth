from django.db import models
from django.utils import timezone

class Minister(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_youth_minister = models.BooleanField(default=False)  # True for youth, False for adults
    position = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {'Youth' if self.is_youth_minister else 'Adult'}"

class Ministry(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ministers = models.ManyToManyField(Minister, related_name='ministries')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    minister = models.ForeignKey(Minister, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.ministry.name} - {self.minister.first_name} {self.minister.last_name}"

class Availability(models.Model):
    minister = models.ForeignKey(Minister, on_delete=models.CASCADE)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.minister.first_name} {self.minister.last_name} - {self.day}"
