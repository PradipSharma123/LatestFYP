# Generated by Django 3.2.9 on 2022-04-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_booking_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delevery', 'Cash On Delevery'), ('Khalti', 'Khalti')], default='Cash On Delevery', max_length=20, null=True),
        ),
    ]
