# Generated by Django 4.1.7 on 2023-03-06 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_documents_document_alter_document_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='anons',
            new_name='ad',
        ),
    ]