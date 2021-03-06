# Generated by Django 2.1.3 on 2020-10-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_evfrequencies'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousElection2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('percent_dems', models.FloatField()),
                ('percent_reps', models.FloatField()),
                ('dem_candiate', models.CharField(max_length=100)),
                ('rep_candidate', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastElections2', to='core.State')),
            ],
        ),
    ]
