# Generated by Django 2.2 on 2019-08-17 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20190817_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='lin_total',
            new_name='line_total',
        ),
    ]
