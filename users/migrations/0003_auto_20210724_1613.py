# Generated by Django 3.2.5 on 2021-07-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=255, null=True),
        ),
    ]
