# Generated by Django 3.0.4 on 2020-03-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggyapp', '0003_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]