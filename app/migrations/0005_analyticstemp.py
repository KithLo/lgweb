# Generated by Django 5.1.4 on 2025-01-24 07:03

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_analytics_isbot_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsTemp',
            fields=[
                ('id', models.CharField(default=app.models.make_id, editable=False, max_length=26, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=45, verbose_name='IP')),
                ('fingerprint', models.CharField(max_length=64)),
                ('language', models.TextField(choices=[('tc', '繁體'), ('sc', '简体')])),
                ('url', models.TextField()),
                ('user_agent', models.TextField()),
                ('referrer', models.TextField()),
            ],
            options={
                'db_table': 'analytics_temp',
            },
        ),
        migrations.AlterField(
            model_name='analytics',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]