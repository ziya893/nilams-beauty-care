from django.conf import settings


def salon_info(request):
    """Makes salon business details available in every template."""
    return {
        'SALON_NAME': settings.SALON_NAME,
        'SALON_ADDRESS': settings.SALON_ADDRESS,
        'SALON_PHONE': settings.SALON_PHONE,
        'SALON_PHONE_RAW': settings.SALON_PHONE_RAW,
        'SALON_WHATSAPP': settings.SALON_WHATSAPP,
    }
