# Generated by Django 4.0.4 on 2022-05-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spent_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('currency', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
