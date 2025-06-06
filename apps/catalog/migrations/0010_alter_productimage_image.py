# Generated by Django 5.2 on 2025-05-06 10:56

import django.utils.timezone
import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_slug_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=django.utils.timezone.now, upload_to='catalog/product/', verbose_name='Category Image'),
            preserve_default=False,
        ),
    ]
