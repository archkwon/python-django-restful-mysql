from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from .models import *


@admin.register(UserInfoModel)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_nm', 'origin_user_pw', 'user_mobile_no', 'cust_code', 'service_agree',
                    'person_agree',
                    'location_agree', 'marketing_agree', 'appro_yn', 'cre_date']
    list_display_links = ['user_id', 'user_nm']
    list_per_page = 20
    list_filter = ['marketing_agree', ('cre_date', DateRangeFilter)]

    search_fields = ['user_id', 'user_nm', 'user_mobile_no', 'cust_code', 'appro_yn']
    ordering = ['-cre_date', 'user_nm']
    exclude = ["user_pw", "device_token", ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["user_id", "user_pw", "origin_user_pw", "service_agree", "location_agree",
                    "marketing_agree", "person_agree", "device_token", "appro_yn", ]
        else:
            return []

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False
