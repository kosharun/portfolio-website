# Generated by Django 4.1.4 on 2022-12-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_description_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.TextField(default=' '),
        ),
    ]
