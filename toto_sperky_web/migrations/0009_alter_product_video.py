# Generated by Django 5.0.4 on 2024-05-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto_sperky_web', '0008_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]