# Generated by Django 3.1.6 on 2021-03-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaproduct',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
