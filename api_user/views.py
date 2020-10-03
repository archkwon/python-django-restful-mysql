from django.http import QueryDict
from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import *


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfoModel.objects.all()
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id', '')

        if user_id:
            queryset.get(user_id=user_id)

        return queryset


class UserInfoSessionView(APIView):

    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwargs):
        user_id = request.GET['user_id']
        user_model = UserInfoModel.objects.get(user_id=user_id)
        serializer = UserInfoSerializer(user_model)

        return JsonResponse({
            'code': True,
            'status': status.HTTP_200_OK,
            'response': serializer.data,
            'message': 'SEARCH_SUCCESS'}, status=status.HTTP_200_OK)


# 로그인 토큰 업데이트
class UpdateTokenAction(APIView):

    # noinspection PyMethodMayBeStatic
    def put(self, request):
        put = QueryDict(request.body)
        user_id = put.get('user_id')
        device_token = put.get('device_token')

        if UserInfoModel.objects.filter(user_id=user_id).exists():
            user_detail = UserInfoModel.objects.get(user_id=user_id)
            user_detail.device_token = device_token
            user_detail.save()

            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'message': 'UPDATE_SUCCESS'}, status=status.HTTP_200_OK)

        return JsonResponse({
            'code': False,
            'status': status.HTTP_200_OK,
            'message': 'FAIL'}, status=status.HTTP_200_OK)