# Generated by Django 3.0.8 on 2020-07-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='codeUrl',
            field=models.URLField(blank=True),
        ),
    ]
