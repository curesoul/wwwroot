# Generated by Django 4.1.1 on 2022-10-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='batch_no',
            field=models.IntegerField(null=True, verbose_name='回号'),
        ),
    ]
