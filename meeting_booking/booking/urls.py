from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('booking/', views.booking_view, name='booking'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
]


