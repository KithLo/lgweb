# Generated by Django 4.2.5 on 2024-12-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image_480',
            field=models.ImageField(blank=True, upload_to='banner/image/'),
        ),
        migrations.AddField(
            model_name='banner',
            name='image_720',
            field=models.ImageField(blank=True, upload_to='banner/image/'),
        ),
    ]
