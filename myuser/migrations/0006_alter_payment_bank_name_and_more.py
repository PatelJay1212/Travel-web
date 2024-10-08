# Generated by Django 5.0.2 on 2024-07-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_alter_book_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='bank_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='beneficiary_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
