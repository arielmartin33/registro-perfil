# Generated by Django 5.1.2 on 2024-11-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(to='accounts.interest', verbose_name='Intereses'),
        ),
    ]
