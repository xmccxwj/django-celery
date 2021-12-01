from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# 指定Django默认配置文件模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shuozhongdian.settings')

app = Celery('abcde')

# 这里指定从django的settings.py里读取celery配置
app.config_from_object('django.conf:settings', namespace='SHUOZHONGDIAN')
# beat：定时任务配置
# 详细可参考参考https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
app.conf.beat_schedule = {
    'schedule_task': {  # 随便取名字
        'task': 'celerytest.task.schedule_task',  # 指定需要定时的任务
        'schedule': crontab(),  # 每天0：00 执行
    },
}
#  发现任务文件每个app下的task.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
