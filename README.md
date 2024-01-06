# Celery Example

# Integration with Celery
## Redis 
Run redis to have both a broker and backend db
```
docker run -p 6379:6379 -it redis/redis-stack:latest
```

## Celery - Worker
Start your celery worker
```
celery -A project.worker.celery worker --loglevel=info --logfile=project/logs/celery.log -n wkr1@hostname
celery -A project.worker.celery worker --loglevel=info --logfile=project/logs/celery.log -n wkr2@hostname
```

## Celery + Flower
Initiate Flower for dashboarding purposes
```
celery --broker=redis://localhost:6379/0 flower --port=5555
```

## FastAPI
Initiate FastAPI service
```
uvicorn app:app --reload
uvicorn app:app --workers 4
```