# Generated by Django 2.2 on 2019-06-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informator', '0003_auto_20190522_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='title',
            new_name='opis',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='zdjecie',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='tresc',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='tytul',
        ),
    ]
