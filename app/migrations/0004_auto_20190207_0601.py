# Generated by Django 2.1.5 on 2019-02-06 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190207_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='confirmation',
            field=models.TextField(default='confirmation', max_length=1000),
        ),
        migrations.AlterField(
            model_name='form1',
            name='hostorganization',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='form1',
            name='multiplicity',
            field=models.TextField(default='multiplicity', max_length=1000),
        ),
        migrations.AlterField(
            model_name='form1',
            name='nationality',
            field=models.TextField(default='nationality', max_length=1000),
        ),
        migrations.AlterField(
            model_name='form1',
            name='passport',
            field=models.TextField(default=1111111111),
        ),
        migrations.AlterField(
            model_name='form1',
            name='placement',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='form1',
            name='root',
            field=models.TextField(default='', max_length=10000),
        ),
    ]