# reservations/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Table, Reservation
from django.utils import timezone
from datetime import timedelta

def map_view(request):
    # Загрузка всех столов для отображения на схеме
    tables = Table.objects.all()
    return render(request, 'reservations/map.html', {'tables': tables})

def booking_view(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        start = request.POST['start_time']
        hours = int(request.POST['hours'])
        # Преобразуем строку в datetime
        from django.utils.dateparse import parse_datetime
        start_dt = parse_datetime(start)
        end_dt = start_dt + timedelta(hours=hours)
        Reservation.objects.create(
            user=request.user,
            table=table,
            start_time=start_dt,
            end_time=end_dt
        )
        return redirect('reservations:payment')
    return render(request, 'reservations/booking.html', {'table': table})

def payment_view(request):
    if request.method == 'POST':
        # здесь интеграция с платёжным шлюзом
        return render(request, 'reservations/payment_success.html')
    return render(request, 'reservations/payment.html')
