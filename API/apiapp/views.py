from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    response=requests.get('https://api.coinbase.com/v2/currencies')
    data1 =response.json()
    data =data1['data']
    context={
        'data':data
    }
    return render(request,'home.html',context)

def one(request):
    response=requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    data1 =response.json()
    data =data1['data']
    context={
        'data':data
    }
    return render(request,'one.html',context)

