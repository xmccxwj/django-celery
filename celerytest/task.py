from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

# 可以指定shared_task的name为任务名称 不指定默认采用方法名
@shared_task
def schedule_task():
    print('定时任务执行了,因为在celery指定了这个名字的任务加入定时任务')



@shared_task(name="send_email")
def send_email():
    print("发送邮箱的普通任务需要手动调用!!!")
    time.sleep(20)
    print('邮箱发送完毕，异步调用不影响主业务')
    return "s"
