# Generated by Django 3.0.7 on 2020-06-24 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tej', '0005_auto_20200625_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultemplate',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]