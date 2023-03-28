# Generated by Django 4.1.7 on 2023-03-28 02:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(upload_to='page_image'),
        ),
    ]
