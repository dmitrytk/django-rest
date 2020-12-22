# Generated by Django 3.1.3 on 2020-12-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201222_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='alt',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='bottom',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='x',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='y',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=25, null=True),
        ),
    ]
