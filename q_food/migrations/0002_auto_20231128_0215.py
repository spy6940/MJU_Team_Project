# Generated by Django 3.2.13 on 2023-11-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q_food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
