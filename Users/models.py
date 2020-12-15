from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    webhook_url = models.TextField(default="")
    branch = models.CharField(default="")

class TimeTable:

    start_time = ''
    end_time = ''
    day = ''
    class_name = ''

    def __init__(self, start_time, end_time, day, class_name):
        self.start_time = start_time
        self.end_time = end_time
        self.day = day
        self.class_name = class_name

