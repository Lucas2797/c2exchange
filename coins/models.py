from django.db import models


class Coin(models.Model):
    cmc_rank = models.PositiveIntegerField()
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=6, unique=True)
    #https://www.gemini.com/cryptopedia/what-are-cryptocurrency-pairs#
    num_market_pairs = models.IntegerField()
    max_supply = models.IntegerField(null=True)
    circulating_supply = models.FloatField(null=True)
    total_supply = models.FloatField(null=True)
    cmc_rank = models.PositiveIntegerField(null=True)
    last_updated = models.DateTimeField()
    price = models.FloatField(null=True)
    volume_24h = models.FloatField(null=True)
    percent_change_3m = models.FloatField(null=True)
    percent_change_1d = models.FloatField(null=True)
    percent_change_7d = models.FloatField(null=True)
    percent_change_30d = models.FloatField(null=True)
    market_cap = models.FloatField(null=True)

    
    def __str__(self):
        return '{}'.format(self.name)




class Tag(models.Model):
    coin = models.ManyToManyField(Coin, related_name='tag')
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=600, null=True)
    
    