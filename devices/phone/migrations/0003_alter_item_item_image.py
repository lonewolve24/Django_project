# Generated by Django 3.2.12 on 2023-08-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(db_column='item_image', default='https://www.shutterstock.com/image-photo/phone-placeholder-that-can-be-260nw-1604743003.jpg', max_length=5000),
        ),
    ]
