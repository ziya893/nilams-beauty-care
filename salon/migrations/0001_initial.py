import django.utils.timezone
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('hair', 'Hair Treatment'), ('face', 'Face Treatment'), ('skin', 'Skin Care'), ('makeup', 'Makeup'), ('bridal', 'Bridal Packages'), ('spa', 'Spa & Body'), ('other', 'Other')], default='other', max_length=20)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in ₹ (INR)', max_digits=8)),
                ('duration_minutes', models.PositiveIntegerField(default=30, help_text='Approx. duration in minutes')),
                ('is_featured', models.BooleanField(default=False, help_text='Show this service on the homepage highlights')),
                ('is_active', models.BooleanField(default=True, help_text='Uncheck to hide this service from the website')),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')),
            ],
            options={
                'ordering': ['category', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.CharField(choices=[('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '01:00 PM'), ('14:00', '02:00 PM'), ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM'), ('18:00', '06:00 PM'), ('19:00', '07:00 PM')], max_length=5)),
                ('message', models.TextField(blank=True, help_text='Any special request from the customer')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='salon.service')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
