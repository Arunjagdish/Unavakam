# Generated by Django 4.2.1 on 2023-06-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_bookingtable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtable',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='bookingtable',
            name='lastname',
        ),
        migrations.AddField(
            model_name='bookingtable',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]