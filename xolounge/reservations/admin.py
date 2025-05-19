from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_cabin', 'capacity')
    list_filter = ('is_cabin',)
    search_fields = ('number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'start_time', 'end_time', 'created_at')
    list_filter = ('table', 'start_time')
    search_fields = ('user__username', 'table__number')
    date_hierarchy = 'start_time'
