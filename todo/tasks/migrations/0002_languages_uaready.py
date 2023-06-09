# Generated by Django 4.1.7 on 2023-04-03 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language_Url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UAReady',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Website_Title', models.CharField(max_length=300)),
                ('Webiste_URL', models.CharField(max_length=500)),
                ('Languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.languages')),
            ],
        ),
    ]
