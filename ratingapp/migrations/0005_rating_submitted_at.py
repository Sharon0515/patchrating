# Generated by Django 3.2.21 on 2023-09-22 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ratingapp', '0004_tester_account_tester_school_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]