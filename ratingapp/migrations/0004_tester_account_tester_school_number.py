# Generated by Django 4.1.2 on 2023-09-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingapp', '0003_alter_rating_image_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tester',
            name='account',
            field=models.CharField(default=138, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tester',
            name='school_number',
            field=models.CharField(default=318, max_length=15),
            preserve_default=False,
        ),
    ]
