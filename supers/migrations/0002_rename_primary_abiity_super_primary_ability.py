# Generated by Django 4.0.2 on 2022-02-21 17:18


# This migration fixed a spelling mistake I had made


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='primary_abiity',
            new_name='primary_ability',
        ),
    ]
