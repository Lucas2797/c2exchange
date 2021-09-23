


export function CoinObject(obj) {
    var new_obj = {
        'Rank': obj['cmc_rank'],
        'Nome': obj['name'],
        'Simbolo': obj['symbol'],
        'Preço': obj['quote']['USD']['price'].toLocaleString("pt-BR"),
        'Volume 24h': obj['quote']['USD']['volume_24h'].toLocaleString("pt-BR"),
        'hor. Update': obj['quote']['USD']['last_updated'],
        'Market Pairs': obj['num_market_pairs'],
        '% 1Hora': obj['quote']['USD']['percent_change_1h'] + "%",
        'platform': '',
        'Máximo': obj['max_supply'],
        'No Mercado': obj['circulating_supply'],
        'Existentes': obj['total_supply'],
        'hor. Update2': obj['last_updated'],
        '% 1Dia': obj['quote']['USD']['percent_change_24h'],
        '% 1Semana': obj['quote']['USD']['percent_change_7d'],
        'Capital': obj['quote']['USD']['market_cap'],
        'slug': obj['slug'],
        'Tags': obj['tags'],
    };
    // var value;
    // Object.entries(new_obj).forEach((key, value) => {
    //     if (value[1] == null) {
    //         console.log(new_obj.value[0])
    //     }
    // })

    if (obj.platform == null) {
        new_obj.platform = ''
    }
    else {
        new_obj.platform = obj.platform.symbol
    }

    return new_obj
}

function currencyFormat(num, dec = 2) {
    return '$' + num.toFixed(dec).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.')
}