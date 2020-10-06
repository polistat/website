# Generated by Django 2.1.3 on 2020-10-06 02:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201002_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatePoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=django.utils.timezone.now)),
                ('percent_trump', models.FloatField()),
                ('percent_biden', models.FloatField()),
                ('n', models.FloatField()),
                ('pollType', models.FloatField()),
                ('pollster', models.CharField(max_length=200)),
                ('moe', models.FloatField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='biden',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='bpi',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='mean',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='state',
            name='trump',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='statepoll',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
    ]