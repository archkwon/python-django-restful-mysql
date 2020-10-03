from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tacar/v1/sign-up/complete/post',views.SignUpCompleteViewSet) #회원가입
router.register(r'tacar/v1/sign-in/post',views.SignInViewSet) #로그인

urlpatterns = [
    path('',include(router.urls)),
    path(r'tacar/v1/sign-up/sms/post', views.SignUpAuthView.as_view()),                #SMS인증번호요청
    path(r'tacar/v1/sign-up/sms/confirm/post', views.SignUpAuthConfirmView.as_view()), #SMS인증번호확인
    path(r'tacar/v1/sign-up/id/get',views.SignUpIdCheckView.as_view()) ,               #아이디중복체크
]
