# Generated by Django 4.1.1 on 2022-10-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixb', '0009_alter_item_m_percent_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='m_percent_type',
            field=models.IntegerField(choices=[(0, '300'), (1, '100'), (2, '50')], default=0, verbose_name='M%数值'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tb_unit',
            field=models.IntegerField(choices=[(0, 'kgf/cm2'), (1, 'Mpa')], default=0, verbose_name='TB单位'),
        ),
    ]
