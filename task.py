from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
import time
import sys

# 定义一个celery对象
# shuozhongdian_celery 为这个celery改的名字 随便都可以
# broker:表示任务队列的位置
# backend:任务完成后结果存放的位置
# 其它参数 后面详解
app = Celery('shuozhongdian_celery', broker='redis://127.0.0.1:6379/6', backend='redis://127.0.0.1:6379/7')


# 普通任务 由 方法名 send_email.delay()触发
@app.task
def send_email(level, content):
    print('去数据库根据等级查询用户:' + "_".join(level))
    print('发送的内容为：' + content)
    time.sleep(20)
    print(sys.exc_info())
    print('发送邮箱结束')
    return "send_email success"


# 定时任务 每分钟执行一次 后续详解
@periodic_task(run_every=crontab())
def task():
    print('定时任务 task 开始!!!!!')
    time.sleep(10)
    print('定时任务 task 结束!!!!!')
    return 'task success'
