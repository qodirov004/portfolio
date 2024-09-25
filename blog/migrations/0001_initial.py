# Generated by Django 5.0.7 on 2024-08-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(choices=[('home', 'Asosiy Sahifa'), ('about', 'Biz haqimizda'), ('service', 'Xizmatlar'), ('work', 'Ish'), ('blog', 'Blog'), ('contact', "Bog'lanish")], unique=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['order'],
            },
        ),
    ]