# Generated by Django 4.1 on 2023-01-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='blog_images')),
            ],
        ),
    ]