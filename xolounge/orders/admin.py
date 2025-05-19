# orders/admin.py

from django.contrib import admin
from .models import Review
from reservations.models import Reservation  # правильный импорт

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'reservation__table__number')
    readonly_fields = ('created_at',)

# Если хотите в админке видеть сами бронь и столы,
# регистрируйте их в reservations/admin.py (как мы делали ранее),
# а здесь оставьте только Review.
