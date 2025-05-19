from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    is_cabin = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField(default=4)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
