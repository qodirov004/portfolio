# Generated by Django 5.0.7 on 2024-08-21 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_aboutme_personalinfo_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='profile',
        ),
    ]
