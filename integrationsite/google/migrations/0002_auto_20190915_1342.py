# Generated by Django 2.2.3 on 2019-09-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
