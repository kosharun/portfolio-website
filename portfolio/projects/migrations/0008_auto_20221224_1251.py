# Generated by Django 3.1 on 2022-12-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_github_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(default=' '),
        ),
    ]
