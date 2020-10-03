from . import views
from django.urls import path, include


urlpatterns = [
    path(r'tacar/v1/driver/location/get', views.DriverLocationView.as_view()), #특정기사위치정보
]
