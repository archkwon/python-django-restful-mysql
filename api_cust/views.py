from django.http.response import JsonResponse
from rest_framework import viewsets, status

from .serializers import *


class CustInfoViewSet(viewsets.ViewSet):
    queryset = CustInfoModel.objects.all()
    serializer_class = CustInfoSerializer

    def list(self, request):
        keyword = request.GET['keyword']

        queryset = CustInfoModel.objects.filter(
            buysale__exact='매출처',
            delyn__exact='N',
            compname__icontains = keyword).order_by('code')

        serializer = CustInfoSerializer(queryset, many=True)
        return JsonResponse({
            'code': True,
            'status': status.HTTP_200_OK,
            'response': serializer.data,
            'message': 'SEARCH_SUCCESS'}, status=status.HTTP_200_OK)

