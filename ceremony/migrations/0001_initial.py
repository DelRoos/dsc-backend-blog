# Generated by Django 3.1.2 on 2020-12-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('banner', models.URLField(blank=True, max_length=500)),
                ('date_event', models.DateTimeField(auto_now_add=True)),
                ('date_pub', models.DateTimeField(auto_now=True)),
                ('chapter_url', models.URLField(blank=True, max_length=500)),
                ('slug', models.SlugField(default='', editable=False, max_length=200, unique=True)),
            ],
        ),
    ]
