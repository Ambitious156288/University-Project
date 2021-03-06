# Generated by Django 2.2 on 2019-05-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powiadomienia', '0008_auto_20190504_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powiadomienie',
            name='grupaOdbiorcow',
        ),
        migrations.RemoveField(
            model_name='powiadomienie',
            name='typPowiadomienia',
        ),
        migrations.AddField(
            model_name='powiadomienie',
            name='kategoria',
            field=models.CharField(choices=[('testowe', 'testowe'), ('Przypomnienie o wydarzeniu', 'Przypomnienie'), ('Ważne informacje', 'Ważne'), ('Konkursy', 'Konkurs'), ('Inne', 'Inne')], default='testowe', max_length=40),
        ),
        migrations.AddField(
            model_name='powiadomienie',
            name='odbiorcy',
            field=models.CharField(choices=[('wszyscy', 'Wszyscy'), ('politechnika', 'Politechnika'), ('uniwersytet', 'Uniwersytet'), ('pozostali', 'Pozostali')], default='Wszyscy', max_length=40),
        ),
    ]
