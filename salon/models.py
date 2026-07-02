from django.db import models
from django.utils import timezone


class Service(models.Model):
    """A single service offered at the salon, e.g. 'Gold Facial' under
    the 'Face Treatment' category."""

    CATEGORY_CHOICES = [
        ('hair', 'Hair Treatment'),
        ('face', 'Face Treatment'),
        ('skin', 'Skin Care'),
        ('makeup', 'Makeup'),
        ('bridal', 'Bridal Packages'),
        ('spa', 'Spa & Body'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price in ₹ (INR)")
    duration_minutes = models.PositiveIntegerField(default=30, help_text="Approx. duration in minutes")
    is_featured = models.BooleanField(default=False, help_text="Show this service on the homepage highlights")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this service from the website")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    @property
    def duration_display(self):
        hours, minutes = divmod(self.duration_minutes, 60)
        if hours and minutes:
            return f"{hours}h {minutes}m"
        if hours:
            return f"{hours}h"
        return f"{minutes} min"


class Appointment(models.Model):
    """A booking request submitted by a customer through the website."""

    TIME_SLOT_CHOICES = [
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='appointments')
    preferred_date = models.DateField()
    preferred_time = models.CharField(max_length=5, choices=TIME_SLOT_CHOICES)
    message = models.TextField(blank=True, help_text="Any special request from the customer")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        service_name = self.service.name if self.service else "General Enquiry"
        return f"{self.full_name} - {service_name} on {self.preferred_date}"
