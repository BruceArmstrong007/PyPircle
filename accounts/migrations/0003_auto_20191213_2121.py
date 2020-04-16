# Generated by Django 3.0 on 2019-12-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='register',
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.CharField(choices=[('active', 'active'), ('In-active', 'In-active')], default='In-active', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
