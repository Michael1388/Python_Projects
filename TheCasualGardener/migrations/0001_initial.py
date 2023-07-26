# Generated by Django 2.2.5 on 2023-02-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=60)),
                ('last_name', models.CharField(blank=True, default='', max_length=60)),
                ('e_mail', models.CharField(blank=True, default='', max_length=90)),
                ('vegetable', models.CharField(choices=[('Lettuce', 'leaf'), ('Tomato', 'Red'), ('Eggplant', 'purple,black')], max_length=60, null=True)),
                ('description', models.TextField(blank=True, default='Enter comments here', max_length=255)),
            ],
        ),
    ]