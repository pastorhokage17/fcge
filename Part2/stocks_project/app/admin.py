from typing import Iterable
from django.contrib import admin
from .models import Investor, Stock, StockOrder

# Register your models here.
admin.site.register(Investor)
admin.site.register(Stock)
admin.site.register(StockOrder)
