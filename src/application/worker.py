from celery import Celery, Task
from application import celery_config
from celery.schedules import crontab

from datetime import datetime

def create_celery_app(app):
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls = FlaskTask)
    celery_app.config_from_object(celery_config)
    celery_app.set_default()
    celery_app.conf.beat_schedule = {
        'daily-report': {
            'task': 'application.tasks.generate_report',
            'schedule': crontab(minute=0, hour=0),  # Midnight every day
            'args': ('daily',),
        },
        'weekly-report': {
            'task': 'application.tasks.generate_report',
            'schedule': crontab(minute=0, hour=0, day_of_week=1),  # Midnight every Monday
            'args': ('weekly',),
        },
        'monthly-report': {
            'task': 'application.tasks.generate_report',
            'schedule': crontab(minute=0, hour=0, day_of_month=1),  # Midnight on the 1st day of the month
            'args': ('monthly',),
        },
        # 'test_scheduler': {
        #     'task': 'application.tasks.sum',
        #     'schedule': crontab(minute='*/2'), # run every two minutes
        # }
}
    return celery_app
