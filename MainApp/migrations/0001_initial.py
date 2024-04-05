# Generated by Django 5.0.4 on 2024-04-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('notes_date', models.DateField(auto_now_add=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('header_file', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post_file', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
    ]