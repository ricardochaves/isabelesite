# Generated by Django 2.2.7 on 2020-08-30 20:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200822_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='text_about_me',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto Sobre Mim'),
        ),
    ]
