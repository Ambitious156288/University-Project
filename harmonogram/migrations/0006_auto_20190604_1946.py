# Generated by Django 2.2 on 2019-06-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harmonogram', '0005_auto_20190604_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koncert',
            name='rodzaj_wydarzenia',
            field=models.CharField(choices=[('TK', 'Tydzień Kultury i Nauki'), ('TS', 'Tydzień Sportu'), ('KO', 'Koncerty')], default='KO', max_length=2),
        ),
    ]
