# Generated by Django 4.2 on 2024-09-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('plate', models.CharField(max_length=255)),
                ('driver', models.CharField(max_length=255)),
            ],
        ),
    ]
