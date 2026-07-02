from django.urls import path
from . import views

app_name = 'salon'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
]
