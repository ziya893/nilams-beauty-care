import logging
import urllib.parse
import urllib.request

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_booking_notifications(appointment):
    _send_email_notification(appointment)
    _send_whatsapp_notification(appointment)


def _format_details(appointment):
    service_name = appointment.service.name if appointment.service else "General Enquiry"
    return (
        f"Name: {appointment.full_name}\n"
        f"Phone: {appointment.phone_number}\n"
        f"Email: {appointment.email or '-'}\n"
        f"Service: {service_name}\n"
        f"Date: {appointment.preferred_date}\n"
        f"Time: {appointment.get_preferred_time_display()}\n"
        f"Message: {appointment.message or '-'}"
    )


def _send_email_notification(appointment):
    if not settings.EMAIL_HOST_USER or not settings.SALON_NOTIFY_EMAIL:
        return
    subject = f"New booking: {appointment.full_name} on {appointment.preferred_date}"
    message = "New appointment booking received!\n\n" + _format_details(appointment)
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.SALON_NOTIFY_EMAIL],
            fail_silently=True,
        )
    except Exception:
        logger.exception("Failed to send booking email notification")


def _send_whatsapp_notification(appointment):
    if not settings.CALLMEBOT_PHONE or not settings.CALLMEBOT_APIKEY:
        return
    service_name = appointment.service.name if appointment.service else "General Enquiry"
    text = (
        f"New booking!\n{appointment.full_name} ({appointment.phone_number})\n"
        f"{service_name}\n{appointment.preferred_date} at {appointment.get_preferred_time_display()}"
    )
    params = urllib.parse.urlencode({
        'phone': settings.CALLMEBOT_PHONE,
        'text': text,
        'apikey': settings.CALLMEBOT_APIKEY,
    })
    url = f"https://api.callmebot.com/whatsapp.php?{params}"
    try:
        urllib.request.urlopen(url, timeout=10)
    except Exception:
        logger.exception("Failed to send WhatsApp booking notification")