# Generated by Django 4.0.6 on 2022-08-14 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('contracts', '0003_alter_contract_created_on_alter_contract_payment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contract', to='clients.client'),
        ),
    ]
