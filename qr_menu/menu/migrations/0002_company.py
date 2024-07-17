# Generated by Django 5.0.3 on 2024-07-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('logo', models.ImageField(upload_to='logos/')),
                ('background_image', models.ImageField(upload_to='backgrounds/')),
            ],
        ),
    ]
