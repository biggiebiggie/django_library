# Generated by Django 3.0.4 on 2020-04-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_auto_20200330_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='loan_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
