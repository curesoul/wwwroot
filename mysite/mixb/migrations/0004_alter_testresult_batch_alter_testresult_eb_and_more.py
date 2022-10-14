# Generated by Django 4.1.1 on 2022-10-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixb', '0003_alter_testresult_batch_alter_testresult_eb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='batch',
            field=models.IntegerField(blank=True, null=True, verbose_name='回数'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='eb',
            field=models.FloatField(blank=True, null=True, verbose_name='EB'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='fmax',
            field=models.FloatField(blank=True, null=True, verbose_name='Fmax'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='fmin',
            field=models.FloatField(blank=True, null=True, verbose_name='Fmin'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='hs',
            field=models.FloatField(blank=True, null=True, verbose_name='HS'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='m_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='M %'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='mv',
            field=models.FloatField(blank=True, null=True, verbose_name='门尼值'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='scorch',
            field=models.FloatField(blank=True, null=True, verbose_name='焦烧'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='sg',
            field=models.FloatField(blank=True, null=True, verbose_name='SG'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='t10',
            field=models.FloatField(blank=True, null=True, verbose_name='T10'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='t90',
            field=models.FloatField(blank=True, null=True, verbose_name='T90'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='tb',
            field=models.FloatField(blank=True, null=True, verbose_name='TB'),
        ),
    ]
