# Generated by Django 4.1.1 on 2022-10-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_monthlist_day_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlist',
            name='day_month',
            field=models.DateField(verbose_name='出表时间'),
        ),
    ]
