# Generated by Django 4.2.5 on 2023-09-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
