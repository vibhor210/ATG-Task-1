# Generated by Django 4.0.3 on 2022-04-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
