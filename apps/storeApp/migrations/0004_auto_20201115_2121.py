# Generated by Django 2.2 on 2020-11-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0003_auto_20201115_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productImages/'),
        ),
    ]