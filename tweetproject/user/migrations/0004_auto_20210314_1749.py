# Generated by Django 3.0.2 on 2021-03-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210314_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
