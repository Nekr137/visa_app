# Generated by Django 2.1.5 on 2019-02-12 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190213_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nationality',
            old_name='n',
            new_name='nationality',
        ),
    ]
