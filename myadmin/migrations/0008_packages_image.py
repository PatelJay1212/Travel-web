# Generated by Django 5.0.2 on 2024-06-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0007_remove_packages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='image',
            field=models.ImageField(default=1, upload_to='package_pics'),
            preserve_default=False,
        ),
    ]
