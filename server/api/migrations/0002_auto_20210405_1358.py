# Generated by Django 3.1.7 on 2021-04-05 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellcase',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='api.well'),
        ),
        migrations.AlterField(
            model_name='wellperforation',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perforations', to='api.well'),
        ),
        migrations.AlterModelTable(
            name='wellcase',
            table='cases',
        ),
        migrations.AlterModelTable(
            name='wellperforation',
            table='perforations',
        ),
        migrations.AlterModelTable(
            name='wellpump',
            table='pumps',
        ),
    ]