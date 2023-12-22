# Generated by Django 4.2.7 on 2023-11-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPs', '0003_wordspic'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SkillName', models.CharField(max_length=30, unique=True)),
                ('SkillDec', models.TextField(max_length=288)),
            ],
        ),
        migrations.DeleteModel(
            name='WordsPic',
        ),
    ]