from django.contrib import admin
from . models import Coin, Tag



class CoinConfig(admin.ModelAdmin):
    list_display = ('cmc_rank', 'name', 'symbol', 'num_market_pairs', 'max_supply', 'circulating_supply', 'total_supply', 'cmc_rank', 'last_updated', 'name', 'name')


class TagConfig(admin.ModelAdmin):
    list_display = ( 'name', 'description')



admin.site.register(Coin, CoinConfig),
admin.site.register(Tag, TagConfig),
