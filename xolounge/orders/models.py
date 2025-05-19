# orders/models.py
from django.db import models
from reservations.models import Reservation
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pros = models.TextField(blank=True)
    cons = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
