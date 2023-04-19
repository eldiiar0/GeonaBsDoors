# Generated by Django 4.2 on 2023-04-15 18:29

from django.db import migrations, models
import doors.models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0006_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='extra_img1',
            field=models.ImageField(blank=True, upload_to=doors.models.image_upload_path),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_img2',
            field=models.ImageField(blank=True, upload_to=doors.models.image_upload_path),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_img3',
            field=models.ImageField(blank=True, upload_to=doors.models.image_upload_path),
        ),
    ]