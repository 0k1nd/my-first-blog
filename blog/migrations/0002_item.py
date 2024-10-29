# Generated by Django 4.2.16 on 2024-10-29 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(blank=django.utils.timezone.now)),
            ],
        ),
    ]
