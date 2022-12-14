# Generated by Django 4.1 on 2022-08-29 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_company_options_alter_device_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.CharField(max_length=26, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_device_id', message='Custom Device PK (ex. nrf-12312980-3138-123123)', regex='^[a-zA-Z]{3}-\\d{8}-\\d{4}-\\d{6}$')]),
        ),
    ]
