# Generated by Django 4.1.4 on 2022-12-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20221222_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_detail',
            field=models.TextField(default=' '),
        ),
    ]
