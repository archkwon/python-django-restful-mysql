import time, json, uuid, datetime, requests, bcrypt

from api_order.models import OrderMasterModel, User
from module import fcm_tacar
from tacar_api.settings import base
from django.utils import timezone
from django.http import QueryDict
from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .sets import *
from .utils import *
from .serializers import *
from api_user.models import UserInfoModel
from api_cust.models import CustInfoModel
from api_user.serializers import UserInfoSerializer


# 회원가입 휴대폰인증단계 #
class SignUpAuthView(APIView):

    # noinspection PyMethodMayBeStatic
    def post(self, request, *args, **kwargs):
        to_user_mobile_no = request.POST.get('user_mobile_no', '')
        purpose_code = request.POST.get('purpose_code', 'signup')

        if to_user_mobile_no is None:
            return JsonResponse({
                'code': False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'REQUIRED USER_MOBILE_NO'}, status=status.HTTP_400_BAD_REQUEST)

        veri_count = UserVeriCodeModel.objects.filter(
            user_mobile_no=to_user_mobile_no,
            cre_date__gte=timezone.now() - datetime.timedelta(minutes=base.NAVER_SMS_TIME_LIMIT)
        ).count()

        if veri_count > 5:
            return JsonResponse({
                'code': False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'REQUEST_COUNT_LIMIT'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            from_mobile_num = base.NAVER_CALL_NUMBER
            api_url = base.NAVER_SMS_API_URL
            api_uri = base.NAVER_SMS_API_URI
            access_key = base.NAVER_ACCESS_KEY
            secret_key = bytes(base.NAVER_SECRET_KEY, 'UTF-8')

            timestamp = str(int(time.time() * 1000))
            string_to_sign = "POST " + api_uri + "\n" + timestamp + "\n" + access_key

            signature = fnc_make_signature(string_to_sign, secret_key)

            headers = {
                'Content-Type': "application/json; charset=UTF-8",
                'x-ncp-apigw-timestamp': timestamp,
                'x-ncp-iam-access-key': access_key,
                'x-ncp-apigw-signature-v2': signature
            }

            four_code = fnc_verification_code(4)
            body_json = {'type': "SMS",
                         'contentType': "COMM",
                         'from': from_mobile_num,
                         'content': "[(주)무진오토라이프] 인증번호 [" + four_code + "] 를 입력해주세요.",
                         'messages': [{"to": to_user_mobile_no}]}

            response = requests.post(api_url, headers=headers, data=json.dumps(body_json))

            # 인증번호 저장
            veri_json = {'uniq_id': str(uuid.uuid4()),
                         'user_mobile_no': to_user_mobile_no,
                         'verification_code': four_code}

            veri_serializer = UserVeriCodeSerializer(data=veri_json)

            if veri_serializer.is_valid():
                veri_serializer.save()

            # 가입목적 저장
            purpose_json = {'uniq_id': str(uuid.uuid4()),
                            'user_mobile_no': to_user_mobile_no,
                            'purpose_code': purpose_code}

            purpose_serializer = UserPurposeInfoSerializer(data=purpose_json)

            if purpose_serializer.is_valid():
                purpose_serializer.save()

            # 인증번호 로그저장
            sms_log_json = {'uniq_id': str(uuid.uuid4()),
                            'user_mobile_no': to_user_mobile_no,
                            'api_type': "SMS",
                            'response_json': str(response.json())}

            sms_log_serializer = NaverCloudLogSerializer(data=sms_log_json)

            if sms_log_serializer.is_valid():
                sms_log_serializer.save()

            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'expire_time': str(base.NAVER_SMS_TIME_LIMIT),
                'message': 'SMS_NUMBER_SUCCESS'}, status=status.HTTP_200_OK)


# 회원가입 휴대폰인증처리 #
class SignUpAuthConfirmView(APIView):

    # noinspection PyMethodMayBeStatic
    def post(self, request, *args, **kwargs):
        user_mobile_no = request.POST.get('user_mobile_no', '')
        verification_code = request.POST.get('verification_code', '')

        if user_mobile_no is None:
            return JsonResponse({
                'code': False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'REQUIRED USER_MOBILE_NO'}, status=status.HTTP_400_BAD_REQUEST)

        if verification_code is None:
            return JsonResponse({
                'code': False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'REQUIRED VERIFICATION_CODE'}, status=status.HTTP_400_BAD_REQUEST)

        latest_veri_list = UserVeriCodeModel.objects.filter(user_mobile_no=user_mobile_no).order_by(
            'user_mobile_no', '-cre_date')[:1]

        if latest_veri_list[0].verification_code == verification_code:

            # 인증번호 입력 3분제한
            time_limit = timezone.now() - datetime.timedelta(minutes=base.NAVER_SMS_TIME_LIMIT)
            time_limit_info = UserVeriCodeModel.objects.filter(
                user_mobile_no=user_mobile_no,
                verification_code=verification_code,
                cre_date__gte=time_limit
            )

            if time_limit_info:
                return JsonResponse({
                    'code': True,
                    'status': status.HTTP_200_OK,
                    'message': 'CONFIRM_SUCCESS'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({
                    'code': False,
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'EXPIRE_AUTH_TIME'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({
                'code': False,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'FAIL_AUTH_NUMBER'}, status=status.HTTP_400_BAD_REQUEST)


# 회원가입 아이디중복체크 #
class SignUpIdCheckView(APIView):

    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwargs):
        user_id = request.GET['user_id']

        try:
            user_model = UserInfoModel.objects.get(user_id=user_id)
            if user_model.user_id:
                return JsonResponse({
                    'code': True,
                    'status': status.HTTP_200_OK,
                    'message': 'EXIST_USER_ID'}, status=status.HTTP_200_OK)

        except UserInfoModel.DoesNotExist:
            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'message': 'AVAILABLE_USER_ID'}, status=status.HTTP_200_OK)


# 회원가입 완료 json.dumps(query_dict) #
class SignUpCompleteViewSet(viewsets.ViewSet):
    queryset = UserInfoModel.objects.all()
    serializer_class = UserInfoSerializer

    # noinspection PyMethodMayBeStatic
    def create(self, request, *args, **kwargs):
        query_dict = QueryDict(request.body)

        if CustInfoModel.objects.filter(code__iexact=query_dict.get("cust_code")).exists():
            if UserInfoModel.objects.filter(user_id__iexact=query_dict.get("user_id")).exists():
                return JsonResponse({
                    'code': False,
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'EXIST_USER_ID'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user_json = user_by_json_mapper(query_dict)
                user_serializer = UserInfoSerializer(data=user_json)
                user_serializer.is_valid(raise_exception=True)
                user_serializer.save()

                cust_json = cust_by_json_mapper(query_dict)
                requests.put(url=base.MUZIN_ERP_API_URL + "/tacar/v1.0/cust/put",
                             data=json.dumps(cust_json),
                             headers=base.REQUESTS_HEADER)

                user_list = User.objects.filter(token__isnull=False)

                fcmTacar = fcm_tacar.FcmTacar()
                registration_ids = []
                for tokens in user_list:
                    print(tokens.token)
                    registration_ids.append(tokens.token)

                message_title = "### 모바일 주문 회원가입 요청 ###</br>클릭해서 회원가입 승인을 검토해주세요"
                message_body = str('sign_up')
                fcmTacar.multiFCMPush(message_title, message_body, registration_ids)

                return JsonResponse({
                    'code': True,
                    'status': status.HTTP_200_OK,
                    'message': 'INSERT_SUCCESS'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'message': 'CUST_NOT_EXIST'}, status=status.HTTP_200_OK)


# 로그인 #
class SignInViewSet(viewsets.ViewSet):
    queryset = UserInfoModel.objects.all()
    serializer_class = UserInfoSerializer

    # noinspection PyMethodMayBeStatic
    def create(self, request, *args, **kwargs):
        query_dict = QueryDict(request.body)

        if UserInfoModel.objects.filter(user_id__iexact=query_dict.get("user_id")).exists():

            user_model = UserInfoModel.objects.get(user_id=query_dict.get("user_id"))

            if bcrypt.checkpw(query_dict.get("user_pw").encode('UTF-8'), user_model.user_pw.encode('UTF-8')):
                user_model.device_token = query_dict.get("device_token")
                user_model.save()

                request.session['user_id'] = query_dict.get("user_id")
                request.session['user_pw'] = query_dict.get("user_pw")

                user_serializer = UserInfoSerializer(user_model)

                if user_model.appro_yn == "Y":
                    return JsonResponse({
                        'code': True,
                        'status': status.HTTP_200_OK,
                        'response': user_serializer.data,
                        'message': 'LOGIN_SUCCESS'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({
                        'code': True,
                        'status': status.HTTP_200_OK,
                        'message': 'SIGN_UP_WAIT'}, status=status.HTTP_200_OK)

            return JsonResponse({
                'code': True,
                'status': status.HTTP_200_OK,
                'message': 'LOGIN_FAIL'}, status=status.HTTP_200_OK)

        return JsonResponse({
            'code': True,
            'status': status.HTTP_200_OK,
            'message': 'LOGIN_FAIL'}, status=status.HTTP_200_OK)
