# Generated by Django 2.0.4 on 2018-04-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('expirydate', models.DateField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('medicine_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
