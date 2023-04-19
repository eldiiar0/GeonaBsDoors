# Generated by Django 4.2 on 2023-04-12 21:57

from django.db import migrations, models
import doors.models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0005_remove_door_glazing_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=doors.models.image_upload_path)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
