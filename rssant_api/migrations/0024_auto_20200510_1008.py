# Generated by Django 2.2.12 on 2020-05-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0023_feed_response_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='reverse_url',
            field=models.TextField(blank=True, help_text='倒转URL', null=True),
        ),
        migrations.AddIndex(
            model_name='feed',
            index=models.Index(fields=['reverse_url'], name='rssant_api__reverse_ddd20d_idx'),
        ),
    ]