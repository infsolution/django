# Generated by Django 2.0 on 2018-11-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0003_auto_20181120_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
