# Generated by Django 3.2.16 on 2023-01-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20230119_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activo_hasta_month',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activo_hasta_year',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pagado_hasta_month',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pagado_hasta_year',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
