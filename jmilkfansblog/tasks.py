from jmilkfansblog.extensions import celery


@celery.task()
def log(msg):
    return msg


@celery.task()
def multiply(x, y):
    return x * y
