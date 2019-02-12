# Generated by Django 2.1.5 on 2019-02-12 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_groupmembers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('placement', models.TextField()),
                ('rout', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='dates',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ships'),
        ),
    ]
