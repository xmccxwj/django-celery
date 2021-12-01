import task
import datetime


def send_email_to_level():
    import time
    start = time.time()
    print("1. 接收前台参数，数据处理巴拉巴拉")

    print("2. 调用celery...完成业务")
    # 可以获得返回值 后续会讲解
    result = task.send_email.delay(level=('2', '3'), content="shuozhongdian@gmail.com")
    print("3. 因为celery是异步的这里可以直接返回，提交成功，后台处理发送中，celery睡了20秒 这里查看下结束时间")
    print("耗时：%s 秒 " % (time.time() - start), ',当前时间为: %s' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 调用下方法
if __name__ == '__main__':
    send_email_to_level()
