from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from project.worker import do_stuff_1, do_stuff_2
from dotenv import load_dotenv
import os
import time

load_dotenv()
os.environ["CELERY_BROKER_URL"] = os.getenv('CELERY_BROKER_URL')
os.environ["CELERY_RESULT_BACKEND"] = os.getenv('CELERY_RESULT_BACKEND')

app = FastAPI()

@app.get("/do_stuff_1")
async def do_stuff_1__endpoint():
    task = do_stuff_1.apply_async((4, 5, ))
    task_result = AsyncResult(task.id).get()
    result = {
        "task_id": task.id,
        "task_status": "SUCCESS",
        "task_result": task_result["result"]
    }
    return JSONResponse(result)

@app.get("/do_stuff_2")
async def do_stuff_2_endpoint():
    task = do_stuff_2.apply_async((4, 5, ))
    task_result = AsyncResult(task.id).get()
    result = {
        "task_id": task.id,
        "task_status": "SUCCESS",
        "task_result": task_result["result"]
    }
    return JSONResponse(result)

@app.get("/do_stuff_1_async")
async def do_stuff_1__endpoint():
    # task = do_stuff_1.delay()
    task = do_stuff_1.apply_async((4, 5,))
    return JSONResponse({"task_id": task.id})

@app.get("/do_stuff_2_async")
async def do_stuff_2_endpoint():
    # task = do_stuff_2.delay()
    task = do_stuff_2.apply_async((4, 5,))
    return JSONResponse({"task_id": task.id})

#### Default endpoints
@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)

@app.get("/health_check")
async def root():
    return {"message": "healthy"}