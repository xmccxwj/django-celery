from django.urls import path, include, re_path
from .views import celery_test

urlpatterns = [
    re_path(r'^celerytest/', celery_test.as_view()),
]
