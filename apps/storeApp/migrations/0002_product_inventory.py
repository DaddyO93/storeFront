# Generated by Django 2.2 on 2020-11-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
