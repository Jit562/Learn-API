# Generated by Django 4.0.1 on 2022-05-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=13, null=True),
        ),
    ]
