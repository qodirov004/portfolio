# Generated by Django 5.0.7 on 2024-08-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_partfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subtitle', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='partfolio',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='partfolio',
            name='title',
        ),
    ]