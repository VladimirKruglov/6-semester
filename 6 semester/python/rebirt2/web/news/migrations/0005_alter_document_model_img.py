# Generated by Django 4.1.7 on 2023-04-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_document_model_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='model_img',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
