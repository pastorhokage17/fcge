from email.policy import default
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

MAX_BALANCE = 10000

class Stock(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        unique=True,
        max_length=32,
        null=True
    )
    price = models.IntegerField(
        default=100
    )
    # class Meta:
    #     db_table = 'Stocks'

    def __str__(self):
        return self.name


class Investor(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    total_stock_amount = models.PositiveIntegerField(
        default=0,
        editable=False
    )

    balance = models.PositiveIntegerField(
        default= MAX_BALANCE,
        editable=False
    )

    def __str__(self):
        return self.username.username

    def reset(self):
        self.total_stock_amount = 0
        self.balance = 10000
        self.save()

        so = StockOrder.objects.all()
        for obj in so:
            obj.quantity = 0
            obj.save()

    def updateInvestor():
        inv = Investor.objects.all().get()
        so  = StockOrder.objects.all()
        p = 0
        q = MAX_BALANCE
        for obj in so:
            p += obj.stock.price * obj.quantity
            inv.total_stock_amount = p
        else:
            pass
        balance = q - inv.total_stock_amount
        if balance >= 0:
            inv.balance = balance    
            inv.save()
        else:
            pass

    def buyStock(amount, stockId):
        amount = int(amount)
        p = amount
        if amount > 0:
            so_query = StockOrder.objects.get(id=stockId)
            amount += so_query.quantity
            so_query.quantity = amount
            so_query.save()
            Investor.updateInvestor()            

        else:
            pass
    
    def sellStock(amount, stockId):
        amount = int(amount)
        p = amount
        if amount > 0:
            so_query = StockOrder.objects.get(id=stockId)
            diff = so_query.quantity - amount
            if(diff >= 0):
                so_query.quantity = diff

                inv = Investor.objects.all().get()
                price = so_query.stock.price
                amount *= price
                inv.total_stock_amount -= amount
                so_query.save()
                Investor.updateInvestor()
        else:
            pass


class StockOrder(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    stock = models.OneToOneField(
        Stock,
        null=True,
        on_delete=models.CASCADE
    )
    investor = models.ForeignKey(
        Investor,
        null=True,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=0
    )



