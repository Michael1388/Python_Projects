# Generated by Django 2.1.5 on 2023-02-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_auto_20230210_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Ms.', 'Ms'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], max_length=60, null=True),
        ),
    ]
