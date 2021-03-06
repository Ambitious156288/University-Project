# Generated by Django 2.2 on 2019-06-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harmonogram', '0004_auto_20190527_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koncert',
            old_name='nazwa',
            new_name='miejsce_wydarzenia',
        ),
        migrations.RenameField(
            model_name='koncert',
            old_name='tydzien',
            new_name='rodzaj_wydarzenia',
        ),
        migrations.RenameField(
            model_name='koncert',
            old_name='image',
            new_name='zdjecie',
        ),
        migrations.AddField(
            model_name='koncert',
            name='nazwa_wydarzenia',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
