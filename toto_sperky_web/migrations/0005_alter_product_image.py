# Generated by Django 5.0.4 on 2024-04-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto_sperky_web', '0004_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]