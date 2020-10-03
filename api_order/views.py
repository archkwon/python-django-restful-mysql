import json
import uuid

import requests
from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from api_cust.models import CustInfoModel
from api_user.models import UserInfoModel
from module import fcm_tacar
from tacar_api.settings import base
from .serializers import *
from .sets import *


# 주문기본정보 #
class OrderMasterViewSet(viewsets.ViewSet):
    queryset = OrderMasterModel.objects.all()
    serializer_class = OrderMasterSerializer

    # noinspection PyMethodMayBeStatic
    def create(self, request, *args, **kwargs):
        request_json = JSONParser().parse(request)

        try:
            user_model = UserInfoModel.objects.get(user_id__exact=request_json['user_id'])

            if user_model.user_id:
                order_code = fnc_order_generate_code()
                master_json = order_master_by_json_mapper(request_json, order_code, user_model)

                order_master_serializer = OrderMasterSerializer(data=master_json)
                order_master_serializer.is_valid(raise_exception=True)
                order_master_serializer.save()

                for rows in request_json['order_list']:
                    detail_json = {
                        'uniq_id': str(uuid.uuid4()),
                        'order_code': order_code,
                        'order_seq': OrderDetailModel.objects.filter(
                            order_code__order_code__exact=order_code).count() + 1,
                        'part_info': rows['part_info'],
                        'part_qty': rows['part_qty'],
                        'part_type': rows['part_type'],
                    }

                    order_detail_serializer = OrderDetailSerializer(data=detail_json)
                    order_detail_serializer.is_valid(raise_exception=True)
                    order_detail_serializer.save()

                requests.put(url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/order/car/sync",
                             data=json.dumps(master_json),
                             headers=base.REQUESTS_HEADER)

                user_list = User.objects.filter(token__isnull=False)

                fcmTacar = fcm_tacar.FcmTacar()
                registration_ids = []
                for tokens in user_list:
                    registration_ids.append(tokens.token)

                customerData = CustInfoModel.objects.get(code=user_model.cust_code)
                questionList = OrderMasterModel.objects.filter(state_cd='N')
                message_title = str(customerData.compname) + " 문의가 접수되었습니다.<br/>남은 모바일 미처리 문의 총 : ( " + str(
                    questionList.count()) + " ) 건<br/>"
                message_body = str(order_code)
                fcmTacar.multiFCMPush(message_title, message_body, registration_ids)

                return JsonResponse({
                    'code': True,
                    'status': status.HTTP_200_OK,
                    'message': 'INSERT_SUCCESS'}, status=status.HTTP_200_OK)

        except UserInfoModel.DoesNotExist:
            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'message': 'NOT_EXIST_USER_ID'}, status=status.HTTP_200_OK)


# 주문상세정보 #
class OrderDetailViewSet(viewsets.ViewSet):
    queryset = OrderMasterModel.objects.all()
    serializer_class = OrderMasterSerializer


# 고객주문 #
class OrderCompleteView(APIView):
    # noinspection PyMethodMayBeStatic
    def post(self, request, *args, **kwargs):
        request_json = JSONParser().parse(request)

        response_json = requests.post(url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/order/complete/post",
                                      data=json.dumps(request_json),
                                      headers=base.REQUESTS_HEADER).json()

        return JsonResponse(response_json, status=status.HTTP_200_OK)


# 문의내역 #
class OrderStatementListView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        user_id = request.GET['user_id']
        user_model = UserInfoModel.objects.get(user_id=user_id)

        response_json = requests.get(
            url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/order/statement/list?cust_code="+user_model.cust_code,
            headers=base.REQUESTS_HEADER).json()

        return JsonResponse(response_json, status=status.HTTP_200_OK, safe=False)


# 문의상세내역
class OrderStatementGetView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        order_code = request.GET['order_code']

        response_json = requests.get(
            url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/order/statement/get?order_code="+order_code,
            headers=base.REQUESTS_HEADER).json()

        return JsonResponse(response_json, status=status.HTTP_200_OK, safe=False)


# 주문내역
class OrderRequestListView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        user_id = request.GET['user_id']
        user_model = UserInfoModel.objects.get(user_id=user_id)

        response_json = requests.get(
            url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/order/request/list?cust_code="+user_model.cust_code,
            headers=base.REQUESTS_HEADER).json()

        return JsonResponse(response_json, status=status.HTTP_200_OK, safe=False)
