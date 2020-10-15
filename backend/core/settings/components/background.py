from datetime import timedelta

from celery.schedules import crontab

CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE = "normal"
CELERY_DEFAULT_ROUTING_KEY = "default"

CELERY_TASK_RESULT_EXPIRES = 3600

CELERYBEAT_SCHEDULE = {
    "celery.backend_cleanup": {
        "task": "celery.backend_cleanup",
        "schedule": timedelta(seconds=300),
        "args": (),
    },
    "periodic": {
        "task": "geo_data.tasks.add",
        "schedule": timedelta(seconds=5),
        "args": (4, 5),
    },
}
