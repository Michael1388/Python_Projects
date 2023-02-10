# Generated by Django 2.1.5 on 2023-02-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_auto_20230210_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Ms.', 'Ms'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], max_length=60, null=True),
        ),
    ]
