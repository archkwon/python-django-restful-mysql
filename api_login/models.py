from django.db import models


class UserVeriCodeModel(models.Model):
    uniq_id = models.CharField(primary_key=True, max_length=50, verbose_name='고유아이디')
    user_mobile_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='휴대폰번호')
    verification_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='SMS인증코드')
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        managed = False
        db_table = 'tb_tacar_veri_code'
        verbose_name = "SMS인증번호코드"
        verbose_name_plural = "SMS인증번호코드"


class NaverCloudLogModel(models.Model):
    uniq_id = models.CharField(primary_key=True, max_length=50, verbose_name='고유아이디')
    user_mobile_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='휴대폰번호')
    api_type = models.CharField(max_length=20, blank=True, null=True, verbose_name='API타입')
    response_json = models.TextField(blank=True, null=True, verbose_name='응답Json파일')
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        managed = False
        db_table = 'tb_tacar_naver_log'
        verbose_name = "네이버클라우드로그정보"
        verbose_name_plural = "네이버클라우드로그정보"


class UserPurposeInfoModel(models.Model):
    uniq_id = models.CharField(primary_key=True, max_length=50, verbose_name='고유아이디')
    user_mobile_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='휴대폰번호')
    purpose_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='가입목적')
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        managed = False
        db_table = 'tb_tacar_purpose_info'
