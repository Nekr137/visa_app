# Generated by Django 2.1.5 on 2019-02-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='additionalinfo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
