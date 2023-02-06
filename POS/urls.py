from django.urls import path
from POS import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/',views.checkout,name='checkout'),
    path('EmployeeManagement',views.EmployeeManagement,name='EmployeeManagement'),
    path('StockManagement',views.stockmanagement,name='StockManagement'),
    path('ProfitManagement',views.profitmanagement,name='ProfitManagement'),
    
    
]

import scheduler