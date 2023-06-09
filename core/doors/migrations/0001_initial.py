# Generated by Django 4.2 on 2023-04-07 14:19

from django.db import migrations, models
import django.db.models.deletion
import doors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=doors.models.image_upload_path)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=doors.models.image_upload_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doors.category')),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('cover', models.CharField(max_length=255)),
                ('color_canvas', models.CharField(max_length=255)),
                ('color_patina', models.CharField(max_length=255)),
                ('glazing', models.BooleanField(blank=True)),
                ('image', models.ImageField(upload_to=doors.models.image_upload_path)),
                ('description', models.TextField()),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doors.subcategory')),
            ],
        ),
    ]
