# Generated by Django 3.0.4 on 2020-05-21 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggyapp', '0014_auto_20200522_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='info',
            new_name='slug',
        ),
    ]