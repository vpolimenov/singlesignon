# Generated by Django 2.2.3 on 2019-09-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0002_auto_20190915_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]