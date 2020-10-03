import requests
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from tacar_api.settings import base


# 기사위치정보
class DriverLocationView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        user_id = request.GET['user_id']

        bacha_response_json = requests.get(url=base.MUZIN_ERP_API_URL  + "/tacar/v1.0/driver/location/get?user_id="+user_id,
                     headers=base.REQUESTS_HEADER).json()

        driver_list = bacha_response_json['response']

        driver_response_json = requests.get(url=base.KIN_DRIVER_API_URL  + "/v1/driver/api/location/recent/get?driver_list="+driver_list,
                     headers=base.REQUESTS_HEADER).json()

        return JsonResponse({
            'code': True,
            'status': status.HTTP_200_OK,
            'response': driver_response_json,
            'message': 'SEARCH_SUCCESS'}, status=status.HTTP_200_OK)
