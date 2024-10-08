# Generated by Django 5.0.2 on 2024-06-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_packages_username_alter_packages_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='days',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='image',
            field=models.ImageField(default=1, upload_to='package_pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='nights',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
