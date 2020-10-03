from rest_framework import serializers
from .models import UserInfoModel


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoModel
        fields = ('user_id', 'user_nm', 'user_pw', 'origin_user_pw', 'user_mobile_no',
                  'cust_code', 'service_agree', 'location_agree', 'person_agree',
                  'marketing_agree', 'device_token', 'appro_yn', 'cre_date', 'upt_date')
