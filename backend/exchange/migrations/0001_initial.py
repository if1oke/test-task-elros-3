# Generated by Django 5.0.3 on 2024-03-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ton', models.PositiveIntegerField()),
                ('btc', models.PositiveIntegerField()),
            ],
        ),
    ]
