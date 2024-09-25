# Generated by Django 5.0.7 on 2024-08-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_contact_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSingle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='profile_image/')),
                ('title', models.CharField(max_length=100, null=True)),
                ('subtitle', models.CharField(max_length=50, null=True)),
                ('text1', models.CharField(max_length=100, null=True)),
                ('text2', models.CharField(max_length=100, null=True)),
                ('text3', models.CharField(max_length=100, null=True)),
                ('text4', models.CharField(max_length=100, null=True)),
                ('text5', models.CharField(max_length=100, null=True)),
                ('text6', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
