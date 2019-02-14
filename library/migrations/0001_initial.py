# Generated by Django 2.1.7 on 2019-02-14 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('book_type', models.CharField(choices=[('MGZ', 'MAGAZINE'), ('RSP', 'RESEARCH PAPER'), ('EBK', 'EBOOK'), ('OTH', 'OTHER')], max_length=3)),
                ('genre', models.CharField(choices=[('TECH', 'TECHNOLOGY'), ('SCIN', 'SCIENCE'), ('FICT', 'FICTION'), ('REFR', 'REFERENCE')], max_length=4)),
                ('isbn', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('is_issued', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_start_dt', models.DateTimeField()),
                ('issue_end_dt', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]