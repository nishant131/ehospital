# Generated by Django 2.0.2 on 2018-03-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
