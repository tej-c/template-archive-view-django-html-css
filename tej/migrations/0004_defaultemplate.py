# Generated by Django 3.0.7 on 2020-06-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tej', '0003_auto_20200624_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='defaultemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.CharField(max_length=200)),
            ],
        ),
    ]
