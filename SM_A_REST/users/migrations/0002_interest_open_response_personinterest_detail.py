# Generated by Django 4.0.3 on 2022-08-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='open_response',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personinterest',
            name='detail',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
