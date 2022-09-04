from apps.home.models import Nav, Banner
from apps.home.serializers import NavModelSerializer, BannerModelSerializer

from utils import constants
from utils.views import CacheListAPIView


class NavHeaderListAPIView(CacheListAPIView):
    """顶部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(CacheListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by(
        "orders", "-id")[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer


class BannerListAPIView(CacheListAPIView):
    """轮播广告视图"""
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.BANNER_SIZE]
    serializer_class = BannerModelSerializer

