from asyncio.windows_events import NULL
from fnmatch import fnmatch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Stock, StockOrder, Investor
# Create your views here.

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
               

    return render(request, "registration/login.html")     

@login_required(login_url='login-url')
def home(request):
    stocks = Stock.objects.all()
    investor = Investor.objects.all()
    stockorders = StockOrder.objects.all()

    context = {
        'stocks':stocks, 
        'investor':investor, 
        'so':stockorders
    }
    
    if request.method == "POST":
        if 'reset' in request.POST:
            inv = Investor.objects.all().get()
            Investor.reset(inv)
    return render(request,"index.html",context)

@login_required(login_url='login-url')
def trade(request):
    stockorders = StockOrder.objects.all()

    if request.method == "POST":
        a = request.POST['buyStockA']
        b = request.POST['buyStockB']
        c = request.POST['buyStockC']

        if len(a) > 0:
            if 'buy' in request.POST:
                Investor.buyStock(a, 6)
            elif 'sell' in request.POST:
                Investor.sellStock(a, 6)  

        if len(b) > 0:
            if 'buy' in request.POST:
                Investor.buyStock(b, 7)
            elif 'sell' in request.POST:
                Investor.sellStock(b, 7) 

        if len(c) > 0:
            if 'buy' in request.POST:
                Investor.buyStock(c, 8)
            elif 'sell' in request.POST:
                Investor.sellStock(c, 8)       


        return redirect('index')
    return render(request, "trade.html",)



