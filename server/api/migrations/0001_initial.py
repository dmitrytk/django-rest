# Generated by Django 3.1.7 on 2021-06-01 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('type', models.CharField(blank=True, max_length=70, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'fields',
            },
        ),
        migrations.CreateModel(
            name='HorizonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'horizon_types',
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('pad', models.CharField(max_length=70, null=True)),
                ('type', models.CharField(max_length=70, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('alt', models.FloatField(null=True)),
                ('bottom', models.FloatField(null=True)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('x', models.FloatField(null=True)),
                ('y', models.FloatField(null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='api.field')),
            ],
            options={
                'db_table': 'wells',
                'unique_together': {('name', 'field')},
            },
        ),
        migrations.CreateModel(
            name='WellState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_short', models.CharField(max_length=5)),
                ('value_full', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'well_states',
            },
        ),
        migrations.CreateModel(
            name='WellWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_short', models.CharField(max_length=5)),
                ('value_full', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'well_work_types',
            },
        ),
        migrations.CreateModel(
            name='WellPump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('md', models.FloatField(null=True)),
                ('rate', models.FloatField(null=True)),
                ('diameter', models.FloatField(null=True)),
                ('well', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.well')),
            ],
            options={
                'db_table': 'pumps',
            },
        ),
        migrations.CreateModel(
            name='WellPerforation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perforator_type', models.CharField(max_length=70, null=True)),
                ('hole_diameter', models.FloatField(null=True)),
                ('holes_per_meter', models.FloatField(null=True)),
                ('top_md', models.FloatField()),
                ('bot_md', models.FloatField()),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perforations', to='api.well')),
            ],
            options={
                'db_table': 'perforations',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rate', models.FloatField(null=True)),
                ('dynamic_level', models.FloatField(null=True)),
                ('static_level', models.FloatField(null=True)),
                ('pressure', models.FloatField(null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='api.well')),
                ('work_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rate_work_type', to='api.wellworktype')),
            ],
            options={
                'db_table': 'rates',
            },
        ),
        migrations.CreateModel(
            name='Inclinometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md', models.FloatField()),
                ('inc', models.FloatField(null=True)),
                ('azi', models.FloatField(null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inc', to='api.well')),
            ],
            options={
                'db_table': 'inclinometry',
            },
        ),
        migrations.CreateModel(
            name='Horizon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_short', models.CharField(max_length=10)),
                ('value_full', models.CharField(max_length=70)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.field')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.horizontype')),
            ],
            options={
                'db_table': 'horizons',
            },
        ),
        migrations.CreateModel(
            name='FieldCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('x', models.FloatField(blank=True, null=True)),
                ('y', models.FloatField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='api.field')),
            ],
            options={
                'db_table': 'field_coordinates',
            },
        ),
        migrations.CreateModel(
            name='WellHorizon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_md', models.FloatField(null=True)),
                ('bot_md', models.FloatField(null=True)),
                ('top_tvdss', models.FloatField(null=True)),
                ('bot_tvdss', models.FloatField(null=True)),
                ('horizon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.horizon')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.well')),
            ],
            options={
                'db_table': 'well_horizons',
                'unique_together': {('well', 'horizon')},
            },
        ),
        migrations.CreateModel(
            name='WellCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('diameter', models.FloatField()),
                ('length', models.FloatField(null=True)),
                ('top_md', models.FloatField(null=True)),
                ('bot_md', models.FloatField(null=True)),
                ('cemented', models.BooleanField(null=True)),
                ('cement_top', models.FloatField(null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='api.well')),
            ],
            options={
                'db_table': 'cases',
                'unique_together': {('name', 'well')},
            },
        ),
        migrations.CreateModel(
            name='Mer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('production', models.FloatField(null=True)),
                ('work_hours', models.FloatField(null=True)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mer_state', to='api.wellstate')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mer', to='api.well')),
                ('work_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mer_work_type', to='api.wellworktype')),
            ],
            options={
                'db_table': 'mer',
                'unique_together': {('well', 'date')},
            },
        ),
    ]
