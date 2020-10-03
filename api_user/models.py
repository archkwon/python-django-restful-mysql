from django.db import models

from api_cust.models import CustInfoModel


class UserInfoModel(models.Model):

    YN_CODE = (
        ('N', 'No'),
        ('Y', 'Yes')
    )

    user_id = models.CharField(primary_key=True, max_length=20, verbose_name='아이디')
    user_nm = models.CharField(max_length=20, verbose_name='성명')
    user_pw = models.CharField(max_length=255, verbose_name='비밀번호')
    origin_user_pw = models.CharField(max_length=20, blank=True, null=True, verbose_name='비밀번호원본')
    user_mobile_no = models.CharField(max_length=20, verbose_name='휴대폰번호')
    cust_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='거래처코드')
    service_agree = models.CharField(max_length=2, blank=True, null=True, verbose_name='서비스동의', choices=YN_CODE)
    location_agree = models.CharField(max_length=2, blank=True, null=True, verbose_name='위치수집동의', choices=YN_CODE)
    marketing_agree = models.CharField(max_length=2, blank=True, null=True, verbose_name='마케팅동의', choices=YN_CODE)
    person_agree = models.CharField(max_length=2, blank=True, null=True, verbose_name='개인정보동의', choices=YN_CODE)
    device_token = models.CharField(max_length=255, blank=True, null=True, verbose_name='기기토큰')
    appro_yn = models.CharField(max_length=2, blank=True, null=True, verbose_name='승인여부', choices=YN_CODE)
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        managed = False
        ordering = ('-cre_date', 'user_nm',)
        db_table = 'tb_tacar_user_info'
        verbose_name = "사용자관리"
        verbose_name_plural = "사용자관리"

    """
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()
    """
