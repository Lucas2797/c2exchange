export function Test() {
    console.log('ok')
}



export function CoinObject(obj) {
    var new_obj = {
        'cmc_rank': obj['cmc_rank'],
        'name': obj['name'],
        'symbol': obj['symbol'],
        'price': obj['quote']['USD']['price'].toFixed(2),
        'volume_24h': obj['quote']['USD']['volume_24h'],
        'last_updated': obj['quote']['USD']['last_updated'],
        'num_market_pairs': obj['num_market_pairs'],
        'percent_change_1h': obj['quote']['USD']['percent_change_1h'],
        'platform': '',
        'max_supply': obj['max_supply'],
        'circulating_supply': obj['circulating_supply'],
        'total_supply': obj['total_supply'],
        'last_updated': obj['last_updated'],
        'percent_change_24h': obj['quote']['USD']['percent_change_24h'],
        'percent_change_7d': obj['quote']['USD']['percent_change_7d'],
        'market_cap': obj['quote']['USD']['market_cap'],
        'slug': obj['slug'],
        'tags': obj['tags'],
    };
    // var value;
    // Object.entries(new_obj).forEach((key, value) => {
    //     if (value[1] == null) {
    //         console.log(new_obj.value[0])
    //     }
    // })

    if (obj.platform == null) {
        new_obj.platform = 'none'
    }
    else {
        new_obj.platform = obj.platform.symbol
    }

    return new_obj
}
