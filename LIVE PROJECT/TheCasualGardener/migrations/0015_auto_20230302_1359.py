# Generated by Django 2.2.5 on 2023-03-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0014_auto_20230302_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='subscription',
            field=models.CharField(choices=[('Semi-Annual', 'Semi-Annual'), ('Monthly', 'Monthly'), ('Bi-Weekly', 'Bi-Weekly'), ('Weekly', 'Weekly')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='vegetable',
            field=models.CharField(choices=[('Multi Tomato Mix', 'Multi Tomato Mix'), ('Leafy Vegetable Mix', 'Leafy Vegetable Mix'), ('Eggplant', 'Eggplant'), ('Cherry Tomato', 'Cherry Tomato'), ('Cucumber Eggplant Squash Mix', 'Cucumber Eggplant Squash Mix'), ('Lettuce', 'Lettuce'), ('Cucumber', 'Cucumber')], max_length=60, null=True),
        ),
    ]
