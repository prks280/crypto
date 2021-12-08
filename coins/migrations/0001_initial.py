# Generated by Django 3.2.9 on 2021-12-08 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('created_on', models.DateField()),
                ('rank', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.FloatField(default=0.0)),
                ('high_24_hour', models.FloatField(default=0.0)),
                ('low_24_hour', models.FloatField(default=0.0)),
                ('volume_24_hour', models.FloatField(default=0.0)),
                ('market_cap', models.IntegerField(default=0.0)),
                ('crypto_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.cryptocoin')),
            ],
        ),
    ]
