# Generated by Django 5.1 on 2024-08-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Genero',
            },
        ),
    ]
