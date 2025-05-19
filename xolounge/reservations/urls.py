# reservations/urls.py
from django.urls import path
from . import views

app_name = 'reservations'
urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('book/<int:table_id>/', views.booking_view, name='booking'),
    path('pay/', views.payment_view, name='payment'),
]
