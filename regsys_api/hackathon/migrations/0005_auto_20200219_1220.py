# Generated by Django 2.2.7 on 2020-02-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_auto_20200219_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='slug_image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
