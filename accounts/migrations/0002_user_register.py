# Generated by Django 3.0 on 2019-12-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register',
            field=models.CharField(choices=[('registered', 'registered'), ('unregistered', 'unregistered')], default='unregistered', max_length=15),
        ),
    ]
