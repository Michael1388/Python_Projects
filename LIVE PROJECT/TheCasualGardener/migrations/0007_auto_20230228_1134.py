# Generated by Django 2.2.5 on 2023-02-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0006_auto_20230228_1042'),
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
            field=models.CharField(choices=[('Cucumber', 'Cucumber'), ('Eggplant', 'Eggplant'), ('Lettuce', 'Lettuce'), ('Leafy Vegetable Mix', 'Leafy Vegetable Mix'), ('Cherry Tomato', 'Cherry Tomato'), ('Cucumber Eggplant Squash Mix', 'Cucumber Eggplant Squash Mix'), ('Multi Tomato Mix', 'Multi Tomato Mix')], max_length=60, null=True),
        ),
    ]
