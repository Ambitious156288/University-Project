# Generated by Django 2.2 on 2019-05-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powiadomienia', '0002_powiadomienie_typpowiadomienia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powiadomienie',
            name='typPowiadomienia',
            field=models.CharField(choices=[('0', 'testowe'), ('1', 'rodzaj 1'), ('2', 'rodzaj 2')], max_length=1),
        ),
    ]
