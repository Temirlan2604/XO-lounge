from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:index'), name='logout'),
]
