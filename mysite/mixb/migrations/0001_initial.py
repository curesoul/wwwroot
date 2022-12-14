# Generated by Django 4.1.1 on 2022-10-12 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='缩写')),
                ('name', models.CharField(max_length=255, verbose_name='公司名称')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='品名')),
                ('mv', models.CharField(max_length=255, verbose_name='门尼')),
                ('mv_min', models.FloatField(verbose_name='最小值')),
                ('mv_max', models.FloatField(verbose_name='最大值')),
                ('temperature', models.IntegerField(blank=True, default=100, verbose_name='温度')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mixb.customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '品名清单',
                'verbose_name_plural': '品名清单',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_created=True, verbose_name='添加时间')),
                ('lot', models.IntegerField(verbose_name='批号')),
                ('batch', models.IntegerField(verbose_name='回数')),
                ('packages', models.IntegerField(verbose_name='框数')),
                ('mix_a_lot', models.CharField(blank=True, max_length=6, verbose_name='A炼批号')),
                ('mix_b_lot', models.CharField(blank=True, max_length=6, verbose_name='B炼批号')),
                ('notes', models.CharField(blank=True, max_length=255, verbose_name='备注')),
                ('etd', models.DateField(blank=True, verbose_name='发货日')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixb.item', verbose_name='品名')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField(verbose_name='回数')),
                ('mv', models.FloatField(verbose_name='门尼值')),
                ('shipment_status', models.BooleanField(default=False, verbose_name='出货状态')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mixb.schedule')),
            ],
            options={
                'verbose_name': '检查明细',
                'verbose_name_plural': '检查明细',
            },
        ),
    ]
