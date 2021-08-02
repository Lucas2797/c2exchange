# Generated by Django 3.1.7 on 2021-05-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=60)),
                ('symbol', models.CharField(max_length=6, unique=True)),
                ('num_market_pairs', models.IntegerField()),
                ('max_supply', models.IntegerField(null=True)),
                ('circulating_supply', models.FloatField()),
                ('total_supply', models.FloatField()),
                ('cmc_rank', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('volume_24h', models.FloatField()),
                ('percent_change_3m', models.FloatField()),
                ('percent_change_1d', models.FloatField()),
                ('percent_change_7d', models.FloatField()),
                ('percent_change_30d', models.FloatField()),
                ('market_cap', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=600)),
                ('coin', models.ManyToManyField(related_name='tag', to='coins.Coin')),
            ],
        ),
    ]