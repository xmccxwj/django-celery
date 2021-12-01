from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app. 确保celey被加载
from .celery import app as celery_app   # app对应celery.py中的app

__all__ = ('celery_app',)
