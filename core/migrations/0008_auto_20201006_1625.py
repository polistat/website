# Generated by Django 2.1.3 on 2020-10-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201006_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statepoll',
            name='pollType',
            field=models.CharField(max_length=2),
        ),
    ]
