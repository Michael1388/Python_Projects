# Generated by Django 2.1.5 on 2023-02-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20230207_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Ms.', 'Ms'), ('Mr.', 'Mr.')], max_length=60, null=True),
        ),
    ]
