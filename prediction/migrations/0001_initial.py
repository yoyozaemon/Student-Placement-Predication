# Generated by Django 2.2.6 on 2020-02-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('tenth', models.IntegerField(max_length=100)),
                ('puc', models.IntegerField(max_length=100)),
                ('degree', models.IntegerField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
    ]