# Generated by Django 4.2.1 on 2023-05-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
