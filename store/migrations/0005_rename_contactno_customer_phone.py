# Generated by Django 3.2.5 on 2021-08-05 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210731_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contactno',
            new_name='phone',
        ),
    ]
