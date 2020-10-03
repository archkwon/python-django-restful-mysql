from rest_framework import serializers
from .models import *


class OrderMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMasterModel
        fields = ('order_code', 'order_text', 'order_answer_text', 'order_ymd', 'cust_code',
                  'user_id', 'car_no', 'vin', 'car_name', 'car_year', 'resv_ymd', 'memo_code',
                  'state_cd', 'order_cd', 'cre_date', 'cre_id', 'upt_date', 'upt_id')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetailModel
        fields = ('uniq_id', 'order_code', 'order_seq', 'part_info', 'part_qty',
                  'part_type', 'cre_date', 'upt_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetailModel
        fields = ('id', 'pwd', 'name', 'auth', 'tel',
                  'email', 'color', 'delyn', 'regid', 'regdt', 'modid', 'moddt', 'token')