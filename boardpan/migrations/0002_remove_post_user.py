# Generated by Django 4.0.5 on 2022-06-20 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardpan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
