# Generated by Django 2.1.5 on 2023-02-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20230210_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs.')], max_length=60, null=True),
        ),
    ]