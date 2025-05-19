# orders/views.py
from django.shortcuts import render, get_object_or_404, redirect
from reservations.models import Reservation
from .models import Review

def history_view(request):
    # все резервации текущего пользователя
    reservations = Reservation.objects.filter(user=request.user).order_by('-start_time')
    return render(request, 'orders/history.html', {'reservations': reservations})

def detail_view(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)

    # Обработка отправки отзыва
    if request.method == 'POST':
        pros = request.POST.get('pros', '').strip()
        cons = request.POST.get('cons', '').strip()
        if pros or cons:
            Review.objects.create(
                reservation=reservation,
                user=request.user,
                pros=pros,
                cons=cons
            )
        # После сохранения редиректим на ту же страницу,
        # чтобы не дублировать отзыв при перезагрузке
        return redirect('orders:detail', reservation_id=reservation.id)

    # Если GET — просто рендерим страницу
    items = reservation.orderitem_set.all() if hasattr(reservation, 'orderitem_set') else []
    return render(request, 'orders/detail.html', {
        'reservation': reservation,
        'items': items,
    })
    
