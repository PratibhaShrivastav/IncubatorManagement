# Generated by Django 2.1.7 on 2019-02-14 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='type',
            new_name='room_type',
        ),
    ]
