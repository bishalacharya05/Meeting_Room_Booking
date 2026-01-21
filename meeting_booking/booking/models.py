from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room.name} - {self.date} {self.start_time}-{self.end_time}"