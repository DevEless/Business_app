# Generated by Django 4.2.1 on 2023-05-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0008_alter_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='business_app/img/'),
        ),
    ]
