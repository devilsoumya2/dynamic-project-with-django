# Generated by Django 5.0.1 on 2024-02-29 17:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]