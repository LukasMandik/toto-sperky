# Generated by Django 5.0.4 on 2024-07-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toto_sperky_web', '0018_blog_blogimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created',), 'verbose_name_plural': 'blogs'},
        ),
        migrations.AddField(
            model_name='blogimage',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
