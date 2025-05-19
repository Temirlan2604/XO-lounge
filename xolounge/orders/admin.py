from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'reservation__table__number')
    readonly_fields = ('created_at',)
