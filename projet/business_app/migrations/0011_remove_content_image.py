# Generated by Django 4.2.1 on 2023-05-30 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0010_alter_content_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
    ]