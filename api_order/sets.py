from .utils import *


# 주문기본정보 Request To Json #
def order_master_by_json_mapper(param_json, order_code, user_model):

    result_json = {
        'order_code': order_code,
        'order_text': param_json['order_text'],
        'order_answer_text' : '',
        'order_ymd': fnc_today_datetime('%Y%m%d'),
        'cust_code': user_model.cust_code,
        'user_id': param_json['user_id'],
        'car_no': param_json['car_no'],
        'vin': '',
        'car_name': '',
        'car_year': '',
        'resv_ymd': '',
        'state_cd': 'N',
        'order_cd': 'N',
        'memo_code': 0,
        'cre_id': param_json['user_id'],
        'upt_id': ''
    }
    return result_json


# 주문상세정보 Request To Json #
def order_detail_by_json_mapper(param_json):

    result_json = {
        'order_code': param_json,
        'car_no': param_json['car_no'],
        'order_text': param_json['order_text'],
        'order_ymd': fnc_today_datetime('%Y%m%d'),
        'cust_code': param_json.cust_code.cust_code,
        'user_id': param_json['user_id']
    }
    return result_json
