# Generated by Django 2.1.5 on 2019-02-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_form1_gen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form1',
            old_name='gen',
            new_name='hostorganization',
        ),
        migrations.AddField(
            model_name='form1',
            name='placement',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form1',
            name='rout',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]