# Generated by Django 5.0.4 on 2024-05-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto_sperky_web', '0012_remove_product_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
