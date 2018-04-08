# Generated by Django 2.0.2 on 2018-02-23 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('title_readable', models.CharField(max_length=256)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=20000)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'article',
            },
        ),
    ]
