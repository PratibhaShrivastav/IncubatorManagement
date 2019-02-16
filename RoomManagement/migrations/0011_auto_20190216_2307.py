# Generated by Django 2.1.7 on 2019-02-16 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RoomManagement', '0010_auto_20190216_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatrequest',
            name='request_from',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seat_requests_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seatrequest',
            name='request_to',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='seat_requests_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='seatrequest',
            name='seat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='RoomManagement.Seat'),
        ),
    ]
