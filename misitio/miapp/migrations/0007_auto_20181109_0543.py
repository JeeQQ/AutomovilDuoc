# Generated by Django 2.1.3 on 2018-11-09 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_auto_20181109_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Anno',
            new_name='Año',
        ),
    ]
