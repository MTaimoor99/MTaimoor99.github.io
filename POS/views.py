from urllib import request
from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse
from POS.models import Checkout,GoodEmployee,WeakEmployee
from POS.models import StockManagement
from POS.models import ProfitManagement




# Create your views here.
def home(request):
    items=StockManagement.objects.all()
    if request.method=='POST':
        TotalPrice=request.POST.get('TotalPrice')
        #ItemsBought=request.POST.get('mylist')
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        ProductNames=request.POST.getlist('ItemsBought[]')
        ProductPrices=request.POST.getlist('ItemsPrice[]')
        print("Items bought are:",ProductNames)
        print("Prices of items bought are:",ProductPrices)
        print(TotalPrice,ProductNames,firstname,lastname)
        InsertCheckoutEntry=Checkout(TotalPrice=TotalPrice,ItemsBought=ProductNames,firstname=firstname,lastname=lastname)
        InsertCheckoutEntry.save()
    return render(request,"Home.html",context={"items":items})

def checkout(request):
    if request.method=="POST":
        
        #request.POST will check the "name" attribute of the HTML tag
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        
        ins= Checkout(firstname=firstname,lastname=lastname)
        ins.save()
        print("Data has been written to the DB")
    return render(request,"Checkout.html",{})

def EmployeeManagement(request):
    if request.method=="POST":
        
        EmployeeFirstName=request.POST['FirstName']
        EmployeeSecondName=request.POST['SecondName']
        EmployeeID=request.POST['ID']
        EmployeeFeedback=request.POST['suggestions']
        EmployeeType=request.POST.get('flexRadioDefault')
        print(EmployeeType)
        if EmployeeType=="P":
             ins_good=GoodEmployee(EmployeeFirstName=EmployeeFirstName,EmployeeSecondName=EmployeeSecondName,EmployeeID=EmployeeID)
             ins_good.save()
             print("Your data has been saved to the database")
                
        elif EmployeeType=="W":
             
             ins_weak=WeakEmployee(EmployeeFirstName=EmployeeFirstName,EmployeeSecondName=EmployeeSecondName,EmployeeID=EmployeeID,EmployeeFeedback=EmployeeFeedback)
             ins_weak.save()
             print("Your data has been saved to the database")


    return render(request,"EmployeeManagement.html",{})


def stockmanagement(request):
    if request.method=="POST":
        ItemName=request.POST['ProductName']
        Quantity=request.POST['ProductQuantity']
        if StockManagement.objects.filter(ItemName=ItemName).exists():
            StockManagement.objects.filter(ItemName=ItemName).update(ItemQuantity=F('ItemQuantity')+Quantity)
            print("Data successfully updated")
        else:
            StockUpdate=StockManagement(ItemName=ItemName,ItemQuantity=Quantity)
            StockUpdate.save()
            print("Data succesfully saved")

    return render(request,"StockManagement.html")

#Will display all the profit generated because of the transactions 
def profitmanagement(request):
    queryset = Checkout.objects.all() #Creating an object to access all the elements of the "Checkout" class in the database.
    TotalProfit=0 #The variable that will be displayed
    for object in queryset:
        TotalProfit=(int(object.TotalPrice.split("-",1)[1]))+TotalProfit #Calculates the total profit. The string is first split after the "-" character.
        #The characters after the "-" are converted into an integer, and then they are used to calculate the total profit
    context={'TotalProfit':TotalProfit} 
    #We will pass this dictionary to our ProfitManagement.html template. This will display our total profit.
    # request.session['context'] = context #Save the dictionary using a context to use in another function
    return render(request,"ProfitManagement.html",context)

