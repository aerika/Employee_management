# Generated by Django 2.0.6 on 2018-06-25 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20180625_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.Department'),
        ),
    ]
