# Generated by Django 4.2.7 on 2023-11-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SkillName', models.CharField(max_length=30, unique=True)),
                ('SkillDec', models.TextField(max_length=288)),
            ],
        ),
    ]
