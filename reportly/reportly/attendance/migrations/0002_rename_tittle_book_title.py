# Generated by Django 3.2.8 on 2021-10-26 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tittle',
            new_name='title',
        ),
    ]
