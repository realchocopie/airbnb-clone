# Generated by Django 3.2.5 on 2021-07-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210724_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('KRW', 'KRW')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('EN', 'US'), ('KR', 'KR')], max_length=20),
        ),
    ]
