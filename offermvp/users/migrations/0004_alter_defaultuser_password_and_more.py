# Generated by Django 4.1.6 on 2023-02-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_defaultuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='password',
            field=models.CharField(default='kmdxp6', max_length=60),
        ),
        migrations.AlterField(
            model_name='defaultuser',
            name='test_password',
            field=models.CharField(default='ymy9vo', max_length=60),
        ),
    ]
