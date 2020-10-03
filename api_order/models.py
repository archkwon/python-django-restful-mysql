from django.db import models


class OrderMasterModel(models.Model):
    order_code = models.CharField(primary_key=True, max_length=20, verbose_name='주문코드')
    order_text = models.TextField(blank=True, null=True, verbose_name='주문내용')
    order_answer_text = models.TextField(blank=True, null=True, verbose_name='답변내용')
    order_ymd = models.CharField(max_length=8, blank=True, null=True, verbose_name='주문일시')
    cust_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='거래처코드')
    user_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='사용자아이디')
    vin = models.CharField(max_length=20, blank=True, null=True, verbose_name='차대번호')
    car_no = models.CharField(max_length=10, blank=True, null=True, verbose_name='차량번호')
    car_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='차량명')
    car_year = models.CharField(max_length=10, blank=True, null=True, verbose_name='차량년식')
    resv_ymd = models.CharField(max_length=8, blank=True, null=True, verbose_name='배송예정일자')
    state_cd = models.CharField(max_length=1, blank=True, null=True, verbose_name='진행상태')
    order_cd = models.CharField(max_length=1, blank=True, null=True, verbose_name='주문상태')
    memo_code = models.BigIntegerField(blank=True, null=True, verbose_name='메모코드')
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    cre_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='등록자아이디')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    upt_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='수정자아이디')

    class Meta:
        managed = False
        db_table = 'tb_tacar_order_master'


class OrderDetailModel(models.Model):
    PART_TYPE_CODE = (
        ('A', '정품'),
        ('B', '일반'),
        ('C', '재생')
    )

    uniq_id = models.CharField(primary_key=True, max_length=50, verbose_name='고유아이디')
    order_code = models.ForeignKey(OrderMasterModel, db_column='order_code', on_delete=models.CASCADE,
                                   verbose_name='주문코드')
    order_seq = models.IntegerField(verbose_name='주문순번', default=0)
    part_info = models.CharField(max_length=100, blank=True, null=True, verbose_name='상품정보')
    part_qty = models.IntegerField(blank=True, null=True, verbose_name='상품수량', default=0)
    part_type = models.CharField(max_length=2, blank=True, null=True, verbose_name='상품타입', choices=PART_TYPE_CODE)
    cre_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')
    upt_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    class Meta:
        managed = False
        db_table = 'tb_tacar_order_detail'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=20)
    auth = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7, blank=True, null=True)
    delyn = models.CharField(max_length=1, blank=True, null=True)
    regid = models.CharField(max_length=20, blank=True, null=True)
    regdt = models.DateTimeField(auto_now_add=True)
    modid = models.CharField(max_length=20, blank=True, null=True)
    moddt = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
