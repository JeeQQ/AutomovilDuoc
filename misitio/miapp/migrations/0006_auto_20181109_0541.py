# Generated by Django 2.1.3 on 2018-11-09 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20181109_0537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='NumPuertas',
            new_name='Num_Puertas',
        ),
    ]
