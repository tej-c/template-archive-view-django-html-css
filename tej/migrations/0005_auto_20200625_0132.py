# Generated by Django 3.0.7 on 2020-06-24 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tej', '0004_defaultemplate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultemplate',
            old_name='default',
            new_name='title',
        ),
    ]
