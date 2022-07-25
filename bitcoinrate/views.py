from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
# from django.http import response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from bitcoinrate.models import Bitcoinrate
from bitcoinrate.serializers import BitcoinrateSerializer
from rest_framework.decorators import api_view
import requests
from environ import Env

env = Env()
env.read_env()  # read .env file, if it exists
# required variables
apikey = env("apikey")  # => 'sloria'

@api_view(['GET', 'POST'])
def rateandprice(request):
    # GET Rate of BTC by USD, POST a price of requesting 
    if request.method == 'GET':
        url='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=' + apikey
        rowData = requests.get(url)
        responseData = rowData.json()
        Data = responseData['Realtime Currency Exchange Rate']
        exchangeRate = Data['5. Exchange Rate']
        # print(exchangeRate)
        obj = Bitcoinrate(rate = exchangeRate)
        obj.save()
        return HttpResponse(exchangeRate)
    elif request.method == 'POST':
        amount = request.data.get("amount")
        url='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=' + apikey
        rowData = requests.get(url)
        responseData = rowData.json()
        Data = responseData['Realtime Currency Exchange Rate']
        exchangeRate = Data['5. Exchange Rate']
        price = float(amount) * float(exchangeRate)
        return HttpResponse(price)