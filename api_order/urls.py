from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tacar/v1/order/master', views.OrderMasterViewSet)
router.register(r'tacar/v1/order/detail', views.OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'tacar/v1/order/complete/post', views.OrderCompleteView.as_view()),       #고객주문
    path(r'tacar/v1/order/statement/list', views.OrderStatementListView.as_view()), #문의내역
    path(r'tacar/v1/order/statement/get', views.OrderStatementGetView.as_view()),   #문의내역
    path(r'tacar/v1/order/request/list', views.OrderRequestListView.as_view()),    #주문내역
]
