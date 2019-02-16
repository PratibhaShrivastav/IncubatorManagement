from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_startuplog'),
        ('accounts', '0003_coffee'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='startup',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startup', to='startups.Startup'),
        ),
    ]
