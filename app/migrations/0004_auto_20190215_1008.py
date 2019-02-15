# Generated by Django 2.1.5 on 2019-02-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_organizations_placements'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalinfo',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dates',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nationality',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizations',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placements',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routs',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ships',
            name='default',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
