# Generated by Django 3.2.1 on 2021-05-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=80)),
                ('experience', models.IntegerField()),
                ('date_of_employment', models.DateField()),
                ('date_of_last_vacation', models.DateField()),
                ('is_on_vacation', models.BooleanField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
