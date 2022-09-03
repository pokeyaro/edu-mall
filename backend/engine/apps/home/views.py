from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django_redis import get_redis_connection


# Call log handler
import logging
logger = logging.getLogger("django")


# Create your views here.
class HomeAPIView(APIView):
    def get(self, request):
        """测试代码，测试完成后可以删除"""
        # 测试日志功能
        logger.error("error log")
        logger.info("info log")
        redis = get_redis_connection("sms_code")
        redis.set('test', 'hello world', ex=10)
        test = redis.get('test')
        return Response(test, status.HTTP_200_OK)
