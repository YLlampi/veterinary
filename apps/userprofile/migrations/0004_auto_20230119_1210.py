# Generated by Django 3.2.16 on 2023-01-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20230119_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activo_hasta_month',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activo_hasta_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pagado_hasta_month',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pagado_hasta_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]