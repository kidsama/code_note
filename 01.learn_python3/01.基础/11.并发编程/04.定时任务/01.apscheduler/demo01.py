"""
@Date: 2024/6/12 下午2:09
@Author: liushaowei
@Description: 
"""

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import time

def task1():
    print("running..1111111111111..")
    time.sleep(10)
    print("Task 1 is done.")

def task2():
    print("running..222222222222..")
    time.sleep(5)
    print("Task 2 is done.")

def task3():
    print("running..333333333333..")
    time.sleep(5)
    print("Task 3 is done.")

scheduler = BackgroundScheduler()
runtime = datetime.now() + timedelta(seconds=5)
for i in range(1000):
    scheduler.add_job(task1, 'date', run_date=runtime, max_instances=1)
# scheduler.add_job(task2, 'interval', seconds=2, max_instances=2)
# scheduler.add_job(task3, 'interval', seconds=2, max_instances=2)
scheduler.start()
time.sleep(30)