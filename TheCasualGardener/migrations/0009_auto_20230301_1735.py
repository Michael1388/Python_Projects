# Generated by Django 2.2.5 on 2023-03-01 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0008_auto_20230301_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='subscription',
            field=models.CharField(choices=[('Semi-Annual', 'Semi-Annual'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Bi-Weekly', 'Bi-Weekly')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='vegetable',
            field=models.CharField(choices=[('Multi Tomato Mix', 'Multi Tomato Mix'), ('Lettuce', 'Lettuce'), ('Cherry Tomato', 'Cherry Tomato'), ('Eggplant', 'Eggplant'), ('Leafy Vegetable Mix', 'Leafy Vegetable Mix'), ('Cucumber Eggplant Squash Mix', 'Cucumber Eggplant Squash Mix'), ('Cucumber', 'Cucumber')], max_length=60, null=True),
        ),
    ]