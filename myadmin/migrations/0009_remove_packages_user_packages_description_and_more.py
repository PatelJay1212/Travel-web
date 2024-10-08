# Generated by Django 5.0.2 on 2024-06-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_packages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='user',
        ),
        migrations.AddField(
            model_name='packages',
            name='description',
            field=models.CharField(default=1, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='destination',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
