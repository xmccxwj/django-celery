from django.shortcuts import render
from django.views import View
from .task import send_email
from django.http import JsonResponse


# Create your views here.


class celery_test(View):
    def get(self, request):
        print("手动调用celery异步任务")
        result = send_email.delay()  # 执行异步任务
        print('获得celery执行的结果 %s' % result.get())
        return JsonResponse({'code': 200, 'msg': '成功'}, safe=False)




