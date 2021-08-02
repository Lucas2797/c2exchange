from coins.models import Coin
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import views
from rest_framework.response import Response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint
from .serializers import CoinSerializer, TagSerializer
from accounts.models import Profile, Investiments
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth import get_user_model



@csrf_exempt
def test_view(request):
    if request.method == 'POST':
        print(request.data)
        return redirect('/coins/home')
    else:
        return render(request, 'test.html')



class HomeView(views.APIView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        return render (request, self.template_name)


    def post(self, request):

        seri = CoinSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
        tags = request.data['tags']

        # AQUII## 
        for t in tags:
            seri2 = TagSerializer(data=t)
        if seri2.is_valid():
            seri2.save()

        return redirect('/coins/home')

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


