from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import groupby
from operator import attrgetter

from django.contrib.admin.views.decorators import staff_member_required
from .forms import AppointmentForm
from .models import Appointment, Service
from .notifications import send_booking_notifications


def home(request):
    featured_services = Service.objects.filter(is_active=True, is_featured=True)[:6]
    if not featured_services:
        featured_services = Service.objects.filter(is_active=True)[:6]
    return render(request, 'salon/home.html', {
        'featured_services': featured_services,
    })


def services(request):
    all_services = Service.objects.filter(is_active=True)
    grouped = []
    for category_key, category_label in Service.CATEGORY_CHOICES:
        items = [s for s in all_services if s.category == category_key]
        if items:
            grouped.append({'label': category_label, 'items': items})
    return render(request, 'salon/services.html', {
        'grouped_services': grouped,
    })


def about(request):
    return render(request, 'salon/about.html')


def contact(request):
    return render(request, 'salon/contact.html')


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            send_booking_notifications(appointment)
            messages.success(                request,
                "Thank you! Your appointment request has been received. "
                "We will contact you shortly to confirm."
            )
            return redirect('salon:appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'salon/book_appointment.html', {'form': form})


def appointment_success(request):
    return render(request, 'salon/appointment_success.html')
@staff_member_required(login_url='/admin/login/')
def manage_bookings(request):
    """Staff-only page listing all customer appointment bookings."""
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_status = request.POST.get('status')
        if appointment_id and new_status in dict(Appointment.STATUS_CHOICES):
            Appointment.objects.filter(id=appointment_id).update(status=new_status)
            messages.success(request, "Booking status updated.")
        return redirect('salon:manage_bookings')

    appointments = Appointment.objects.select_related('service').all()
    return render(request, 'salon/manage_bookings.html', {
        'appointments': appointments,
        'status_choices': Appointment.STATUS_CHOICES,
    })