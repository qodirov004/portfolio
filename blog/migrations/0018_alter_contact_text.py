# Generated by Django 5.0.7 on 2024-08-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_contact_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
