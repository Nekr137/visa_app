# Generated by Django 2.1.7 on 2019-02-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_visanumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visanumber',
            name='visanumber',
            field=models.IntegerField(),
        ),
    ]