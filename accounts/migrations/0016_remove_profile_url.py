# Generated by Django 2.1.7 on 2019-02-16 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_profile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='url',
        ),
    ]
