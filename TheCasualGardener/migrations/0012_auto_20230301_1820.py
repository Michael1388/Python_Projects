# Generated by Django 2.2.5 on 2023-03-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0011_auto_20230301_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='subscription',
            field=models.CharField(choices=[('Bi-Weekly', 'Bi-Weekly'), ('Monthly', 'Monthly'), ('Semi-Annual', 'Semi-Annual'), ('Weekly', 'Weekly')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='vegetable',
            field=models.CharField(choices=[('Multi Tomato Mix', 'Multi Tomato Mix'), ('Leafy Vegetable Mix', 'Leafy Vegetable Mix'), ('Eggplant', 'Eggplant'), ('Cucumber Eggplant Squash Mix', 'Cucumber Eggplant Squash Mix'), ('Cucumber', 'Cucumber'), ('Lettuce', 'Lettuce'), ('Cherry Tomato', 'Cherry Tomato')], max_length=60, null=True),
        ),
    ]