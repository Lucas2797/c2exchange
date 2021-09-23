from coins.models import Coin
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import views, permissions
from rest_framework.response import Response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint
from .serializers import CoinSerializer, TagSerializer
from accounts.models import Profile, Investiment
from accounts.serializers import InvestimentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone





class HomeView(views.APIView):
    template_name = 'home.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request, *args, **kwargs):
        return render (request, self.template_name)


    def post(self, request):
        dict_coin = request.data.update(request.data['quote']['USD'])
        seri_coin = CoinSerializer(data=request.data)
        print(request.data)
        if seri_coin.is_valid():
            coin_obj = seri_coin.save()
            tags = request.data['tags']
            print(tags)
            dict_invest = {'one':request.user.profile.id, 'coin':coin_obj.pk, 'payd':request.data['payd'], 'ammount':request.data['ammount']}
            print(dict_invest)
            seri_invest = InvestimentSerializer(data=dict_invest)
            if seri_invest.is_valid():
                seri_invest.save()
            else:
                print(seri_invest.errors)
            for t in tags:
                dict_tag = {'coin':[coin_obj.pk], 'name':t}
                seri_tag = TagSerializer(data=dict_tag)
                if seri_tag.is_valid():
                    tag_obj = seri_tag.save()
                    tag_obj.coin.add(coin_obj)
                else:
                    print(seri_tag.errors)
        else:
            print(seri_coin.errors)
        return redirect('home')

def json_view(request):
    return Response(template_name='data.json', content_type='application/json')

class RestartList(views.APIView):
    
    def get(self, request, *args, **kwargs):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
        'start':'1',
        'limit':'500',
        'convert':'USD',
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'fdc8b069-06f6-4921-b1a2-3c605721acae',
        }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return Response(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            pprint(e)


class TestView(views.APIView):
    permissions = [permissions.IsAuthenticated]

    def get (self, request):
        return Response({"nome": "lucas"})

