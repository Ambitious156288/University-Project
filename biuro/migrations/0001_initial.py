# Generated by Django 2.2 on 2019-05-22 22:52

import datetime
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
            name='LostItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2047)),
                ('contact', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('isAccepted', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='gallery_pics/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
