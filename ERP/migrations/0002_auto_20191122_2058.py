# Generated by Django 2.2.2 on 2019-11-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(),
        ),
    ]
