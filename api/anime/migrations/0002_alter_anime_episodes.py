# Generated by Django 3.2.9 on 2021-11-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(),
        ),
    ]
