# Generated by Django 4.1.6 on 2023-02-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Ms.', 'Ms'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], max_length=60, null=True),
        ),
    ]