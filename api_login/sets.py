import bcrypt
from .utils import *


# 거래처매핑 Request To Json #
def cust_by_json_mapper(query_dict):
    result_json = {
        'code': query_dict.get("cust_code"),
        'user_id': query_dict.get("user_id"),
        'ceoname': query_dict.get("user_nm"),
        'cust_mbtl_no': fnc_special_char_regexp(query_dict.get("user_mobile_no")),
        'zonecode': query_dict.get("cust_zipcode"),
        'address': query_dict.get("cust_addr"),
        'addressdetail': query_dict.get("cust_addr_detail"),
        'divzonecode': query_dict.get("div_zipcode"),
        'divaddress': query_dict.get("div_addr"),
        'divaddressdetail': query_dict.get("div_addr_detail"),
        'modid': fnc_special_char_regexp(query_dict.get("user_mobile_no")),
    }
    return result_json


# 사용자매핑 Request To Json #
def user_by_json_mapper(query_dict):
    result_json = {
        'user_id': query_dict.get("user_id"),
        'user_pw': bcrypt.hashpw(query_dict.get("user_pw").encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8'),
        'origin_user_pw': query_dict.get("user_pw"),
        'user_nm': query_dict.get("user_nm"),
        'user_mobile_no': fnc_special_char_regexp(query_dict.get("user_mobile_no")),
        'service_agree': query_dict.get("service_agree"),
        'person_agree': query_dict.get("person_agree"),
        'location_agree': query_dict.get("location_agree"),
        'marketing_agree': query_dict.get("marketing_agree"),
        'device_token': query_dict.get("device_token"),
        'cust_code': query_dict.get("cust_code"),
        'appro_yn': 'N'
    }
    return result_json
