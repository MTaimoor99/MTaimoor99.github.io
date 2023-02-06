from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
from POS import views
import sys




def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(views.ClearHourlyProfit, trigger='interval', seconds=10) #Running this function every hour.
    # scheduler.add_job(views.ClearDailyProfit, trigger='interval', hours=24) #Running this function once a day.
    # scheduler.add_job(views.ClearWeeklyProfit, trigger='interval', hours=168) #Running this function once a week. 
    # scheduler.add_job(views.ClearMonthlyProfit, trigger='interval', hours=730) #Running this function once a month.
    # scheduler.add_job(views.ClearYearlyProfit, trigger='interval', hours=8760) #Running this function once a year.
    scheduler.start()
    register_events(scheduler)
    
   