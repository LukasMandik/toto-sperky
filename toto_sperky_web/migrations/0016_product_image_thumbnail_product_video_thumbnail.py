# Generated by Django 5.0.4 on 2024-05-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto_sperky_web', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='video_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]