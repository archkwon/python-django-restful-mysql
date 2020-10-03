from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tacar/v1/user', views.UserInfoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path(r'tacar/v1/session/user', views.UserInfoSessionView.as_view()),
    path(r'tacar/v1/update/token', views.UpdateTokenAction.as_view()),
]

