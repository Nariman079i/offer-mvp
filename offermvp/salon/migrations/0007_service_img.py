# Generated by Django 4.1.6 on 2023-04-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_page_service_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Изображение'),
        ),
    ]