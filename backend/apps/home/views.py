from rest_framework.generics import ListAPIView

from apps.home.models import Nav
from apps.home.serializers import NavModelSerializer

from utils import constants


class NavHeaderListAPIView(ListAPIView):
    """顶部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer
