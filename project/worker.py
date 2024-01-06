import os
from celery import Celery
import time
from dotenv import load_dotenv

load_dotenv()

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", os.getenv('CELERY_BROKER_URL'))
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", os.getenv('CELERY_RESULT_BACKEND'))

@celery.task(name="do_stuff_1")
def do_stuff_1(x, y):
    time.sleep(20)
    res = x+y
    return {"result": f"Outcome from do_stuff_1. {x}+{y}={res}"}

@celery.task(name="do_stuff_2")
def do_stuff_2(x, y):
    time.sleep(10)
    res = x-y
    return {"result": f"Outcome from do_stuff_2. {x}-{y}={res}"}