# Generated by Django 5.1.4 on 2025-01-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_message_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='isbot',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='analytics',
            name='country',
            field=models.TextField(blank=True),
        ),
        migrations.AddIndex(
            model_name='analytics',
            index=models.Index(fields=['isbot', 'created_at'], name='analytics_query_idx'),
        ),
    ]
