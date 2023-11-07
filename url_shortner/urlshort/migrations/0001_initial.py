# Generated by Django 4.1 on 2023-11-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=1000)),
                ('short_url', models.CharField(max_length=100)),
            ],
        ),
    ]
