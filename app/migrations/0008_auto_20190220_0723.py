# Generated by Django 2.1.5 on 2019-02-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190219_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='invitation_number',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form2',
            name='invitation_number',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
