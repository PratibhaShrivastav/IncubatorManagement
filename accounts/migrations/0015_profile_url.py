# Generated by Django 2.1.7 on 2019-02-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_coffee_amount_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
