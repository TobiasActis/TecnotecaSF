# Generated by Django 5.0 on 2023-12-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='apellido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='usuarios',
        ),
    ]