# Generated by Django 2.0.13 on 2020-09-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('army_vacation', '0003_washworker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washworker',
            name='date',
            field=models.DateTimeField(),
        ),
    ]