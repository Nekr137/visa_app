# Generated by Django 2.1.5 on 2019-02-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190216_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visanumber', models.IntegerField(default=1)),
            ],
        ),
    ]
