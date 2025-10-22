from celery import Celery
app = Celery('demo', broker='redis://localhost:6379/0')

@app.task
def add(a, b):
    return a + b