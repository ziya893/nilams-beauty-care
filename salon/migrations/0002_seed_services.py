from django.db import migrations


DEFAULT_SERVICES = [
    # category, name, description, price, duration_minutes, is_featured, order
    ('hair', 'Haircut & Styling', 'Precision haircut finished with a professional blow-dry style.', 300, 45, True, 1),
    ('hair', 'Hair Spa', 'Deep conditioning hair spa to repair dry and damaged hair.', 700, 60, True, 2),
    ('hair', 'Hair Colour (Global)', 'Full head hair colour using premium ammonia-friendly products.', 1800, 120, False, 3),
    ('hair', 'Hair Straightening / Smoothening', 'Long-lasting smoothening treatment for frizz-free, silky hair.', 3500, 180, False, 4),
    ('hair', 'Keratin Treatment', 'Keratin protein treatment to strengthen and add shine to hair.', 4500, 180, False, 5),

    ('face', 'Classic Facial', 'Cleansing, exfoliation and massage for fresh, glowing skin.', 500, 45, True, 1),
    ('face', 'Gold Facial', 'Luxurious 24k gold facial for brightening and anti-aging care.', 1200, 60, True, 2),
    ('face', 'Fruit Facial', 'Natural fruit-based facial to nourish and rejuvenate the skin.', 600, 45, False, 3),
    ('face', 'De-Tan Facial', 'Removes sun tan and evens out skin tone.', 550, 45, False, 4),
    ('face', 'Anti-Ageing Facial', 'Targeted treatment to reduce fine lines and improve skin elasticity.', 1500, 60, False, 5),

    ('skin', 'Skin Polishing', 'Full-face skin polishing for a smooth, radiant look.', 800, 45, False, 1),
    ('skin', "Bleach & D-Tan", 'Facial bleach and de-tan combo for instant glow.', 400, 30, False, 2),
    ('skin', 'Threading & Waxing', 'Eyebrow threading and full-arm/leg waxing services.', 250, 30, False, 3),

    ('makeup', 'Party Makeup', 'Glamorous makeup look perfect for parties and events.', 1500, 60, True, 1),
    ('makeup', 'Engagement Makeup', 'Elegant makeup package designed for engagement ceremonies.', 3500, 90, True, 2),
    ('makeup', 'HD Makeup', 'Flawless, camera-ready HD makeup for special occasions.', 2500, 75, False, 3),
    ('makeup', 'Nail Art & Manicure', 'Manicure with creative nail art designs.', 500, 45, False, 4),

    ('bridal', 'Bridal Makeup Package', 'Complete bridal makeover including makeup, hairstyle and draping.', 8000, 180, True, 1),
    ('bridal', 'Pre-Bridal Package', 'Skin and hair prep sessions leading up to the wedding day.', 6000, 240, False, 2),

    ('spa', 'Body Massage', 'Relaxing full-body massage to relieve stress and tension.', 900, 60, False, 1),
    ('spa', 'Body Polishing', 'Full-body exfoliation and polishing for soft, glowing skin.', 1800, 90, False, 2),
]


def seed_services(apps, schema_editor):
    Service = apps.get_model('salon', 'Service')
    for category, name, description, price, duration, is_featured, order in DEFAULT_SERVICES:
        Service.objects.get_or_create(
            name=name,
            category=category,
            defaults={
                'description': description,
                'price': price,
                'duration_minutes': duration,
                'is_featured': is_featured,
                'is_active': True,
                'order': order,
            },
        )


def remove_services(apps, schema_editor):
    Service = apps.get_model('salon', 'Service')
    names = [item[1] for item in DEFAULT_SERVICES]
    Service.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_services, remove_services),
    ]
