# Generated by Django 2.1.7 on 2019-05-04 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('harmonogram', '0002_koncert_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='koncert',
            name='organizator',
        ),
        migrations.AddField(
            model_name='koncert',
            name='organizatorzy',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='koncert',
            name='tydzien',
            field=models.CharField(choices=[('TK', 'Tydzien Kultury'), ('TS', 'Tydzien Sportu'), ('', 'Koncerty')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='koncert',
            name='uczestnicy',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
