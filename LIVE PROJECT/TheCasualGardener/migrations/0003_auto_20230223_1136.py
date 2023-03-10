# Generated by Django 2.2.5 on 2023-02-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0002_auto_20230223_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='subscription',
            field=models.CharField(choices=[('Bi-Weekly', 'Bi-Weekly'), ('Weekly', 'Weekly'), ('Semi-Annual', 'Semi-Annual'), ('Monthly', 'Monthly')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='vegetable',
            field=models.CharField(choices=[('Cucumber', 'Cucumber'), ('Lettuce', 'Lettuce'), ('Eggplant', 'Eggplant'), ('Cherry Tomato', 'Cherry Tomato'), ('Tomato', 'Tomato')], max_length=60, null=True),
        ),
    ]
