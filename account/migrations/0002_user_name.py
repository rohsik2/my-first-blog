# Generated by Django 2.0.13 on 2020-08-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='wow', max_length=10),
            preserve_default=False,
        ),
    ]
