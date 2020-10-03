from rest_framework import serializers
from .models import *


class UserVeriCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVeriCodeModel
        fields = ('uniq_id', 'user_mobile_no', 'verification_code', 'cre_date', 'upt_date')


class NaverCloudLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaverCloudLogModel
        fields = ('uniq_id', 'user_mobile_no', 'api_type', 'response_json', 'cre_date', 'upt_date')


class UserPurposeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPurposeInfoModel
        fields = ('uniq_id', 'user_mobile_no', 'purpose_code', 'cre_date', 'upt_date')
