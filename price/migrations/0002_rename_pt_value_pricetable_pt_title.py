# Generated by Django 3.2.9 on 2021-11-23 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetable',
            old_name='pt_value',
            new_name='pt_title',
        ),
    ]