# Generated by Django 4.2.7 on 2023-11-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteSub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]
