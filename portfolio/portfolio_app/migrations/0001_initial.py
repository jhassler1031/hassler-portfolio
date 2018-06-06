# Generated by Django 2.0.6 on 2018-06-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tech_used', models.CharField(max_length=255)),
                ('github_link', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
