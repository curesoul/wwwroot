# Generated by Django 4.1.1 on 2022-10-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixb', '0011_alter_item_eb_max_alter_item_eb_min'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ('batch',), 'verbose_name': '检查明细', 'verbose_name_plural': '检查明细'},
        ),
        migrations.AlterField(
            model_name='schedule',
            name='etd',
            field=models.DateField(blank=True, null=True, verbose_name='发货日'),
        ),
    ]
