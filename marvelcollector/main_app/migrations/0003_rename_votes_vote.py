# Generated by Django 4.2.3 on 2023-08-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_votes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
