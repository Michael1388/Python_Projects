# Generated by Django 2.2.5 on 2023-03-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheCasualGardener', '0019_auto_20230302_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='subscription',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Bi-Weekly', 'Bi-Weekly'), ('Semi-Annual', 'Semi-Annual'), ('Weekly', 'Weekly')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='vegetable',
            field=models.CharField(choices=[('Cucumber Eggplant Squash Mix', 'Cucumber Eggplant Squash Mix'), ('Multi Tomato Mix', 'Multi Tomato Mix'), ('Cherry Tomato', 'Cherry Tomato'), ('Leafy Vegetable Mix', 'Leafy Vegetable Mix'), ('Eggplant', 'Eggplant'), ('Cucumber', 'Cucumber'), ('Lettuce', 'Lettuce')], max_length=60, null=True),
        ),
    ]
