# Generated by Django 5.1.6 on 2025-04-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_product_vector_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]
