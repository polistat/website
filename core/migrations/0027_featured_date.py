# Generated by Django 2.1.3 on 2020-10-20 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]