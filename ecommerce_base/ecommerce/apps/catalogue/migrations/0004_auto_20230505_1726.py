# Generated by Django 3.2 on 2023-05-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20230505_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Unit',
            new_name='unit_choices',
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.IntegerField(default=1),
        ),
    ]
