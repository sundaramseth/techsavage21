# Generated by Django 3.0.4 on 2020-05-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_auto_20200522_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='shortinfo',
            field=models.CharField(max_length=500),
        ),
    ]