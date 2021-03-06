# Generated by Django 2.0.6 on 2018-06-22 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=30)),
                ('contact_num', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Department')),
            ],
        ),
    ]
