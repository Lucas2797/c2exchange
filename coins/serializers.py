from rest_framework import serializers
from .models import Tag, Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['cmc_rank',
                  'name',
                  'symbol',
                  'num_market_pairs',
                  'max_supply',
                  'circulating_supply',
                  'total_supply',
                  'cmc_rank',
                  'last_updated',
                  'price',
                  'volume_24h',
                  'percent_change_3m',
                  'percent_change_1d',
                  'percent_change_7d',
                  'percent_change_30d',
                  'market_cap']
        

        
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['coin',
                  'name',
                  'description',]
    

