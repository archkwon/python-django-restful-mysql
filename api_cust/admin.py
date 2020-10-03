import math
from .models import *
from api_user.models import UserInfoModel

from rangefilter.filter import DateRangeFilter
from django.contrib import admin

""" 사용안함 
class UserInfoInline(admin.TabularInline):
    model = UserInfoModel

    list_display = ["user_id", "user_nm", "user_mobile_no", "origin_user_pw", "service_agree", "location_agree",
                    "marketing_agree", "person_agree", "cre_date", ]
    readonly_fields = ["user_id", "user_nm", "user_mobile_no", "origin_user_pw", "service_agree", "location_agree",
                    "marketing_agree", "person_agree", "cre_date", ]
    exclude = ["user_pw", "device_token", ]

    can_delete = False
    extra = 1
    max_num = 10
    verbose_name = '거래처사용자'
    verbose_name_plural = '거래처사용자'


    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CustInfoAdmin(admin.ModelAdmin):
    list_display = ['cust_code', 'cust_name', 'cust_mbtl_no', 'cust_addr', 'div_addr', 'del_yn','cre_date',]

    list_display_links = ['cust_code', 'cust_name']
    list_per_page = 20
    list_filter = ['del_yn', ('cre_date', DateRangeFilter)]
    inlines = [UserInfoInline,]
    search_fields = ['cust_code', 'cust_name', 'cust_mbtl_no', 'del_yn',]
    ordering = ['cust_code']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["cust_code", "cre_date",]
        else:
            return []

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CustInfoModel, CustInfoAdmin)

"""