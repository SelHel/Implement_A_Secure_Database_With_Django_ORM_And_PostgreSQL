# Generated by Django 4.0.6 on 2022-08-29 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_sales_contact'),
        ('users', '0003_alter_employee_user'),
        ('contracts', '0004_alter_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(limit_choices_to={'role': 'SALES'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contract', to='users.employee'),
        ),
    ]
