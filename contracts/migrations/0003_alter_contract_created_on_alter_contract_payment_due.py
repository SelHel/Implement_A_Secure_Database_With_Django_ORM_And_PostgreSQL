# Generated by Django 4.0.6 on 2022-08-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_alter_contract_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateField(),
        ),
    ]