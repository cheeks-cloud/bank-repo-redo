# Generated by Django 4.1.6 on 2023-02-13 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='memberAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.IntegerField(verbose_name=16)),
                ('balance', models.IntegerField(verbose_name=16)),
                ('ownerName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='membercardnum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.IntegerField(verbose_name=16)),
                ('cardAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.memberaccounts')),
            ],
        ),
    ]
