from django.contrib import admin
from POS.models import Checkout,GoodEmployee, ProfitManagement,WeakEmployee
from POS.models import StockManagement


# Register your models here.
admin.site.register(Checkout)
admin.site.register(GoodEmployee)
admin.site.register(WeakEmployee)
admin.site.register(StockManagement)
admin.site.register(ProfitManagement)