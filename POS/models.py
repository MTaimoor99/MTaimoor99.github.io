from django.db import models


# Create your models here.
class Checkout(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    ItemsBought=models.TextField(default="")
    TotalPrice=models.TextField(default="")

    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)


class GoodEmployee(models.Model):
    EmployeeFirstName=models.CharField(max_length=30)
    EmployeeSecondName=models.CharField(max_length=30)
    EmployeeID=models.BigIntegerField()

    def __str__(self):
        return "{} {}".format(self.EmployeeFirstName,self.EmployeeSecondName)

class WeakEmployee(GoodEmployee):
    EmployeeFeedback=models.TextField()

    def __str__(self):
        return "{} {}".format(self.EmployeeFirstName,self.EmployeeSecondName)

class StockManagement(models.Model):
    ItemName=models.CharField(max_length=100)
    ItemQuantity=models.BigIntegerField()

    def __str__(self):
        return self.ItemName

class ProfitManagement(models.Model):
    
    day_count=models.BigAutoField(primary_key=True)
    DailyProfit=models.BigIntegerField()
    MonthlyProfit=models.BigIntegerField()
    YearlyProfit=models.BigIntegerField()
