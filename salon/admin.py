from django.contrib import admin
from .models import Service, Appointment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration_minutes', 'is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_active', 'is_featured')
    list_editable = ('price', 'is_featured', 'is_active', 'order')
    search_fields = ('name', 'description')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'service', 'preferred_date', 'preferred_time', 'status', 'created_at')
    list_filter = ('status', 'preferred_date', 'service')
    list_editable = ('status',)
    search_fields = ('full_name', 'phone_number', 'email')
    date_hierarchy = 'preferred_date'
