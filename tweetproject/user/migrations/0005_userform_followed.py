# Generated by Django 3.0.2 on 2021-03-14 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20210314_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='followed',
            field=models.ManyToManyField(blank=True, related_name='hasfollowed', to=settings.AUTH_USER_MODEL),
        ),
    ]
