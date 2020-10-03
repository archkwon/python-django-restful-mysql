import os, binascii
from datetime import datetime


# 주문번호생성
def fnc_order_generate_code():
    now = datetime.now()
    code = now.strftime('%Y%m%d%H%M%S%f')
    return code[:20]


# 오늘날짜
def fnc_today_datetime(pattern):
    today = datetime.now()
    return today.strftime(pattern)


# 주문번호생성-미사용
def fnc_order_generate_key():
    return binascii.hexlify(os.urandom(20)).decode()
