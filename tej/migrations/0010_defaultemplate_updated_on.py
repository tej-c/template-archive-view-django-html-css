# Generated by Django 3.0.7 on 2020-06-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tej', '0009_auto_20200625_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultemplate',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]