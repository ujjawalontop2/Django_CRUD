# Generated by Django 4.1.4 on 2022-12-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default='initial description', max_length=254)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
