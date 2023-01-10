# Generated by Django 4.1.5 on 2023-01-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_featurecrud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
