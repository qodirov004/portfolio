# Generated by Django 5.0.7 on 2024-08-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_blogsingle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsingle',
            name='text1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogsingle',
            name='text2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogsingle',
            name='text3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogsingle',
            name='text4',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogsingle',
            name='text5',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogsingle',
            name='text6',
            field=models.CharField(max_length=255, null=True),
        ),
    ]