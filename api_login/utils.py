import base64
import hashlib
import hmac
import string
import random
import re


# 공통함수 Naver SMS API signature 암호화 #
def fnc_make_signature(string_to_sign, secret_key):
    signStr = bytes(string_to_sign, 'UTF-8')
    string_hmac = hmac.new(secret_key, signStr, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64


# 공통함수 SMS인증번호 #
def fnc_verification_code(num_length):
    string_pool = string.digits
    result = ""
    for i in range(num_length) :
        result += random.choice(string_pool)

    return result


# 공통함수 특수문자제거 #
def fnc_special_char_regexp(keyword):
    result = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', keyword)
    return result
