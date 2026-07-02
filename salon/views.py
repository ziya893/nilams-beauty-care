from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import groupby
from operator import attrgetter

from .forms import AppointmentForm
from .models import Service


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
            form.save()
            messages.success(
                request,
                "Thank you! Your appointment request has been received. "
                "We will contact you shortly to confirm."
            )
            return redirect('salon:appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'salon/book_appointment.html', {'form': form})


def appointment_success(request):
    return render(request, 'salon/appointment_success.html')
