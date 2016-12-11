from jmilkfansblog.extensions import celery


@celery.task()
def log(msg):
    return msg
