# Generated by Django 4.1.1 on 2022-10-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixb', '0008_alter_item_m_percent_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='m_percent_type',
            field=models.IntegerField(choices=[(0, '300'), (1, '100'), (2, '50')], default=0, verbose_name='M%单位'),
        ),
    ]
