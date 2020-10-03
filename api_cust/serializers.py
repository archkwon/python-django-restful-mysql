from rest_framework import serializers
from .models import *


class CustInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustInfoModel
        fields = '__all__'

