# Generated by Django 4.0.3 on 2022-04-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/images')),
                ('category', models.CharField(choices=[('MH', 'Mental Health'), ('HD', 'Heart Disease'), ('C-19', 'Covid-19'), ('Imu', 'Immunization')], default='Mental Health', max_length=20)),
                ('summary', models.TextField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
