# Generated by Django 4.0.6 on 2022-08-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
