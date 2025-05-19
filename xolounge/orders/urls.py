# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.history_view, name='history'),
    path('<int:reservation_id>/', views.detail_view, name='detail'),
]
