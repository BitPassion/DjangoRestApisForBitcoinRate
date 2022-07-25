from apscheduler.schedulers.background import BackgroundScheduler
from bitcoinrate import update
import os

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(update.execute_powershell, 'interval', seconds = 3600)
    scheduler.start()
    