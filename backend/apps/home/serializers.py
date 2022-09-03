from rest_framework import serializers

from apps.home import models


class NavModelSerializer(serializers.ModelSerializer):
    """
    导航菜单的序列化器
    """
    class Meta:
        model = models.Nav
        fields = ["name", "link", "is_http"]
