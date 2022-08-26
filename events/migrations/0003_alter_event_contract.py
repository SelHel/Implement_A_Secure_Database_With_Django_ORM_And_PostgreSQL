# Generated by Django 4.0.6 on 2022-08-26 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_alter_contract_client'),
        ('events', '0002_alter_event_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contracts.contract'),
        ),
    ]
