# Generated by Django 4.0.1 on 2022-01-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
