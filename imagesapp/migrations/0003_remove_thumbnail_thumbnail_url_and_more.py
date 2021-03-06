# Generated by Django 4.0.5 on 2022-06-18 19:16

from django.db import migrations, models
import imagesapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0002_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='original_source',
            field=models.ImageField(blank=True, null=True, upload_to=imagesapp.models.upload_to),
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail_format',
            field=models.CharField(default='png', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail_height',
            field=models.PositiveIntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='thumbnail_width',
            field=models.PositiveIntegerField(default=200),
            preserve_default=False,
        ),
    ]
