# Generated by Django 4.1.1 on 2022-10-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_rename_type_monthlist_type_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlist',
            name='day_month',
            field=models.CharField(max_length=6, verbose_name='出表时间'),
        ),
    ]