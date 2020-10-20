# Generated by Django 2.1.3 on 2020-10-02 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('important', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HouseElection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.IntegerField()),
                ('candidate1name', models.CharField(blank=True, max_length=100)),
                ('candidate1party', models.CharField(blank=True, max_length=100)),
                ('candidate1incumbent', models.BooleanField(default=False)),
                ('candidate2name', models.CharField(blank=True, max_length=100)),
                ('candidate2party', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('party', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SenateElection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate1name', models.CharField(blank=True, max_length=100)),
                ('candidate1party', models.CharField(blank=True, max_length=100)),
                ('candidate1incumbent', models.BooleanField(default=False)),
                ('candidate2name', models.CharField(blank=True, max_length=100)),
                ('candidate2party', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Senator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('party', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='congressional_makeup',
        ),
        migrations.RemoveField(
            model_name='state',
            name='important_congressional_elections',
        ),
        migrations.AddField(
            model_name='senator',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
        migrations.AddField(
            model_name='senateelection',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
        migrations.AddField(
            model_name='representative',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
        migrations.AddField(
            model_name='houseelection',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
        migrations.AddField(
            model_name='demographic',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State'),
        ),
    ]