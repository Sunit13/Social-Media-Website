# Generated by Django 3.0.2 on 2021-03-16 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210317_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog'),
        ),
    ]
