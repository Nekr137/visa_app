# Generated by Django 2.1.5 on 2019-02-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190207_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='familyname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='form1',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='form1',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='form1',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='form1',
            name='passport',
            field=models.TextField(),
        ),
    ]
