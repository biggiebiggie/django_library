# Generated by Django 3.0.4 on 2020-03-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='author',
        ),
    ]
