# Generated by Django 3.0.3 on 2020-04-12 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpoll',
            name='user',
        ),
    ]
