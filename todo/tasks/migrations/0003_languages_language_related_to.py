# Generated by Django 4.1.7 on 2023-04-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_languages_uaready'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='Language_Related_To',
            field=models.CharField(choices=[('', '-- Select --'), ('ENGLISH', 'English'), ('HINDI', 'Hindi'), ('MARATHI', 'Marathi')], default='', max_length=15),
        ),
    ]
